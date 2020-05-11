import os, sys, shutil, os.path
from tkinter import *
from tkinter.filedialog import askopenfilename
# from package.moderator import moderator 
from tkinter.filedialog import asksaveasfile
import cv2
from PIL import Image 
import numpy as np
import pytesseract

def get_string(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)
    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   
    # Blur
    # img = cv2.medianBlur(img, 1)
     
    #  Apply threshold to get image with only black and white
    _,img = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # for i in range(4):
    # Apply dilation and erosion to remove some noise   
    kernel = np.ones((1, 1), np.uint8)    
    # img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    img =  cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    img = cv2.dilate(img, kernel, iterations=1)    
    img = cv2.erode(img, kernel, iterations=1)
    img = cv2.dilate(img, kernel, iterations=5)  
    img = cv2.medianBlur(img,3)
    cv2.imwrite('C:/Users/Hady/Desktop/img-processing-master/test.png', img)
    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(img, lang='eng')
    return result

class gui:
    
    def __init__(self):
        self.master = Tk()    
        self.label=Label(self.master,text='please choose a photo to be processed jpg or png only')
        self.label.pack()
        self.selectFile_button = Button(self.master,text ="select a photo",command = self.handelSelctPhoto)
        self.selectFile_button.pack()
        self.textarea = Text(self.master)
        self.textarea.pack()   
        self.selectFile_button = Button(self.master,text ="save as text file",command = self.saveAsTextFile)
        self.selectFile_button.pack()                    
        self.txt=''
        self.master.mainloop()    

    
    def handelSelctPhoto(self):        
        img = askopenfilename()    
        text = get_string(img)
        self.txt=text
        self.textarea.insert(INSERT,text)
        
    
    def saveAsTextFile(self):
        # textFile = open('file.txt',"w+")
        text = self.textarea.get("1.0","end")
        files = [('All Files', '*.*'),  
             ('Python Files', '*.py'), 
             ('Text Document', '*.txt')] 
        file = asksaveasfile(filetypes = files, defaultextension = files) 


        file.write(text)
        self.textarea.delete("1.0", "end")
        file.close()
    
root= tk.Tk()

t=gui()

root.mainloop()


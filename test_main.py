import os, sys, shutil, os.path
from tkinter import *
from tkinter.filedialog import askopenfilename
# from package.moderator import moderator 
from tkinter.filedialog import asksaveasfile
import cv2
from PIL import Image 
import numpy as np
import pytesseract

src_path = "C:/Users/Hady/Desktop/img-processing-master/"

def get_string(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite(src_path + "removed_noise.png", img)

    #  Apply threshold to get image with only black and white
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image after apply opencv to do some ...
    cv2.imwrite(src_path + "thres.png", img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(src_path + "thres.png"))

    # Remove template file
    #os.remove(temp)

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
    
    

t=gui()




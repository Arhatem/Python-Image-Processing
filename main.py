import os, sys, shutil, os.path
from tkinter import *
from tkinter.filedialog import askopenfilename
# from package.moderator import moderator 
from tkinter.filedialog import asksaveasfile
import cv2
from PIL import Image 
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'



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
        text = pytesseract.image_to_string(img)
        self.txt=text
        self.textarea.insert(INSERT,text)
        
    
    def saveAsTextFile(self):
        
        text = self.textarea.get("1.0","end")
        files = [('All Files', '*.*'),  
             ('Python Files', '*.py'), 
             ('Text Document', '*.txt')] 
        file = asksaveasfile(filetypes = files, defaultextension = files) 


        file.write(text)
        self.textarea.delete("1.0", "end")
        file.close()
    
    

t=gui()




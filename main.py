from tkinter import *
from tkinter.filedialog import askopenfilename
# from package.moderator import moderator 

import cv2
from PIL import Image 
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'



class gui:
    
    master=None
    moderator=None

    def __init__(self):
        self.master = Tk()    
        self.selectFile_button = Button(self.master,text ="select a photo",command = self.handelSelctPhoto)
        self.selectFile_button.pack()
        self.textarea = Text(self.master)
        self.textarea.pack()                       
        self.master.mainloop()    

       
        
    
    def handelSelctPhoto(self):        
        img = askopenfilename()        
        text = pytesseract.image_to_string(img)
        self.textarea.insert(INSERT,text)
        
        
    
    
    

t=gui()
# t.startGui()



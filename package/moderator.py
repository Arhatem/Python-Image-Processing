from tkinter import *
import cv2
from PIL import Image 
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

class moderator:
    textarea=None
    gui=None
    def __init__(self,gui):
        self.gui=gui

    def setTextarea(self,textarea):
        self.textarea=textarea
        

    # def getFilePath(self):

    def turnImgToText(self):
        # img = Image.open('F:\\4th cse asu\\image proccessing project\\mytest.png')
        img = self.gui.getPhotoFile()
        text = pytesseract.image_to_string(img)
        return text

    def showText(self):
        text = self.turnImgToText()
        self.textarea.insert(INSERT,text)

    def notify(self,sender):
        if sender == 'select photo':
            self.turnImgToText()
            self.showText()


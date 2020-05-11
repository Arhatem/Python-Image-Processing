import sys

import cv2
from PIL import Image 
import numpy as np
import pytesseract
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout , QVBoxLayout,QApplication
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QLabel,
    QInputDialog, QApplication,QFileDialog,QPlainTextEdit)

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


class moderator:
    def __init__(self):
        pass

    def process_photo(self,photo):                   
        text = pytesseract.image_to_string(photo)
        return text


class gui:
    def __init__(self):
        self.moderator = moderator()

        self.app = QApplication(sys.argv)

        self.window = QWidget()

        self.window.setWindowTitle('photo to text')

        self.window.setGeometry(100, 100, 280, 80)
        
        self.window.move(60, 15)

        self.hand_writen_btn = QPushButton('hand writen')

        self.hand_writen_btn.clicked.connect(self.handel_photo)

        self.normal_text_btn = QPushButton('normal text')

        self.normal_text_btn.clicked.connect(self.handel_photo)        

        self.save_file_btn = QPushButton('save file')

        self.save_file_btn.clicked.connect(self.save_file)   

        self.layout = QVBoxLayout()

        self.textArea = QPlainTextEdit()

        self.lable=QLabel('please select the photo type')

        self.layout.addWidget(self.lable)

        self.layout.addWidget(self.hand_writen_btn)

        self.layout.addWidget(self.normal_text_btn)

        self.layout.addWidget(self.textArea)    
        
        self.layout.addWidget(self.save_file_btn) 

        self.window.setLayout(self.layout)

        self.window.show()

        sys.exit(self.app.exec_())

    def handel_photo(self):
        photo = self.open_photo_file()
        text=self.moderator.process_photo(photo)
        self.set_textarea_text(text)


    def open_photo_file(self):
        
        file_name = QFileDialog.getOpenFileName(self.window,'open file')
        return file_name[0]

    def set_textarea_text(self,text):
        self.textArea.insertPlainText(text)

    def save_file(self):
        text = self.textArea.toPlainText()
        file_name = QFileDialog.getSaveFileName(self.window, "Save File", '/', '.txt')[0]
        if file_name == "":
            return
        print(file_name)
        file = open(file_name,'w+')
        file.write(text)
        self.textArea.setPlainText('')
        file.close()



    
f = gui()
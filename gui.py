import six
import mkl
import sys
import cv2
from PIL import Image 
import numpy as np
import cv2
import pytesseract
import PyQt5
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout , QVBoxLayout,QApplication
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QLabel,
    QInputDialog, QApplication,QFileDialog,QPlainTextEdit)


class moderator:
    def __init__(self):
        pass

    def process_photo_hand_written(self,photo):
        # Read image with opencv
        img = cv2.imread(photo)
        # Convert to gray
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   
        # Blur
        img = cv2.medianBlur(img, 1)
        # # Apply dilation and open and close to remove some noise   
        kernel = np.ones((1,1), np.uint8)    
        img = cv2.dilate(img, kernel, iterations=1)  
        img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
        img =  cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
        #  Apply threshold to get image with only black and white
        _,img = cv2.threshold(img,100,240,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        cv2.imwrite('C:/Users/Hady/Desktop/img-processing-master/test.png', img)
        # Recognize text with tesseract for python
        result = pytesseract.image_to_string(img, lang='eng')                   
        return result

    def process_photo_normal_written(self,photo):
        # Read image with opencv
        img = cv2.imread(photo)
        # Convert to gray
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   
        # Apply dilation to make it more thin    
        kernel = np.ones((1, 1), np.uint8)    
        img = cv2.dilate(img, kernel, iterations=1)    
        #  Apply threshold to get image with only black and white
        _,img = cv2.threshold(img,0,240,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        # Apply morphology Close to avoid any missing pixels throgh the letters
        img =  cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
        # Recognize text with tesseract for python
        result = pytesseract.image_to_string(img, lang='eng')                  
        return result


class gui:
    def __init__(self):
        self.moderator = moderator()

        self.app = QApplication(sys.argv)

        self.window = QWidget()

        self.window.setWindowTitle('Photo to text')

        self.window.setGeometry(700, 700, 700, 700)
        
        self.window.move(60, 15)

        self.hand_writen_btn = QPushButton('Hand writen')

        self.hand_writen_btn.clicked.connect(self.handel_photo_hand)

        self.normal_text_btn = QPushButton('Normal text')

        self.normal_text_btn.clicked.connect(self.handel_photo_normal)        

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

    def handel_photo_hand(self):
        photo = self.open_photo_file()
        text=self.moderator.process_photo_hand_written(photo)
        self.set_textarea_text(text)

    def handel_photo_normal(self):
        photo = self.open_photo_file()
        text=self.moderator.process_photo_normal_written(photo)
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



    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = gui()
    app.exec()
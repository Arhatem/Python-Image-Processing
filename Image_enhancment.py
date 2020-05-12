
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


imgloc = "C:\\images_samples\\7.jpg"
kernel = np.ones((3,3),np.uint8)
img = cv2.imread(imgloc)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.medianBlur(img, 3)
_,img = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
img = cv2.dilate(img,kernel,iterations = 1)
cv2.imshow('new_img',img)
#cv2.imwrite('C:\\images_samples\\10.jpg', img)
cv2.waitKey(0)

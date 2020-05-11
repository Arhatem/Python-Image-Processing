
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


imgloc = "C:\\images_samples\\hando3.jpg"
img = cv2.imread(imgloc)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.medianBlur(img, 3)
_,img = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('new_img',img)
#cv2.imwrite('C:\\images_samples\\10.jpg', img)
cv2.waitKey(0)
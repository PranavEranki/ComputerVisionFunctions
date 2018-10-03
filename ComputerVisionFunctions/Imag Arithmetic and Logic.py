#IMAGE ARITHMETICS AND LOGC//////////////////////////////
import cv2
import numpy as np

# 500 x 250
img1 = cv2.imread('3D-Matplotlib.png')
img3 = cv2.imread('mainsvmimage.png')
img2 = cv2.imread('mainlogo.png')

#ARITHMETICS
add = img1+img3
add1 = cv2.add(img1, img3)
weighted = cv2.addWeighted(img1, 0.6,img3, 0.4, 0)
cv2.imshow('weighted', weighted)

#LOGIC
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]
#Used to convert image into gray
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
#Used to convert image into binary 0/1 above 220 consider 1
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

#Convert background to white nd image to black
img1_bg = cv2.bitwise_and(roi roi, mask=mask_inv)
#Convert background to black only
img2_fg = cv2.bitwise_and(img2, img2, mask = mask)

#Adding two image
dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols]  = dst

cv2.imshow('res',img1)
cv2.imshow('mask_inv',mask_inv)
cv2.imshow('img1_bg',img1_bg)
cv2.imshow('img2_fg',img2_fg)
cv2.imshow('dst',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

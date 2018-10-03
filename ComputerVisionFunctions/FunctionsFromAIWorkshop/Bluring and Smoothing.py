#BLURRING AND SMOOTHING///////////////////////////////////////////////////
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    
    #HUE SATURATION AND VALUE(hsv) 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0,0,0])
    upper_red = np.array([255,255,255])

    #Mask will show image in 0 or 1(binary)
    mask = cv2.inRange(hsv, lower_red, upper_red)
    #if pixel is in the range it will show color otherwise black
    res = cv2.bitwise_and(frame, frame, mask=mask)

    #SMOOTHING
    kernel = np.ones((15,15), np.float32)/225
    smoothed = cv2.filter2D(res, -1, kernel)

    #BLURRING 
    blur = cv2.GaussianBlur(res, (15,15), 0)
    median = cv2.medianBlur(res, 15)

    #Another way to blur images
    bilateral = cv2.bilateralFilter(res, 15, 75, 75) 
    
    cv2.imshow('frame', frame)
    #cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cv2.imshow('blur', blur)
    cv2.imshow('median', median)
    cv2.imshow('bilateral', bilateral)

    k = cv2.waitKey(5) & 0xFF 
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()

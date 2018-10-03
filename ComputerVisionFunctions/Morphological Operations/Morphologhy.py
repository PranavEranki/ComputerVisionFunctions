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

    kernel = np.ones((15,15), np.uint8)
    #EROSION 
    erosion = cv2.erode(mask, kernel, iterations=1)
    #DILATION
    dilation = cv2.dilate(mask, kernel, iterations=1)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    

    cv2.imshow('frame', frame)
    cv2.imshow('res', res)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

    k = cv2.waitKey(5) & 0xFF 
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()

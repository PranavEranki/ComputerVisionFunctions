#LOADING VIDEO SOURCE //////////////////////////////////////////

import cv2
import numpy as np

#used to capture the VIDEO  with which webcam you are watching now (generally used when having more than one webcam )
cap = cv2.VideoCapture(0)

#fourcc represents Codec 
#used to Save the Video in file name output having video of 20 sec and size of 680x480
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (680, 480))

while True:
    #return the frame after reading
    ret, frame= cap.read()
    
    #Used to convert the image into gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    out.write(frame)
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray )
    
    #Used to exit from frame by pressing letter 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
#Used to release the captured frame 
cap.release()
out.release()
cv2.destroyAllWindows()

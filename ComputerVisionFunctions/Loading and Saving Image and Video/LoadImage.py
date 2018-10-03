import cv2
import numpy as np
import matplotlib.pyplot as plt

## LOADING AND SAVING IMAGES////////////////////////////

img = cv2.imread('rose.jpg', cv2.IMREAD_GRAYSCALE)

#BY Using OpenCV
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

        OR

#### BY uisng plt method
plt.imshow(img, cmap='gray', interpolation = 'bicubic')
plt.plot([50,100],[80,100], 'c', linewidth =5)
plt.show()

###Saving a file
cv2.imwrite('PinkRose.jpg', img)

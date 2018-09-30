try:
    import cv2
    import numpy as np
    import argparse
    import os
    import cv2
    import numpy as np
except:
    print("Necessary packages are not imported.")
    print("Refer to requirements for necessary packages")
    sys.exit()

def exists(image):
    if (os.path.exists(os.path.join(os.getcwd(),image))):
        return True
    else:
        return False

def gaussian(image):
    print("Performing adaptive gaussian thresholding on image given")
    print("Press any key to close the image")

    grayscaled = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 255, 32)
    cv2.imshow('Original input',image)
    cv2.imshow('Gaussian thresholding active', gaus)
    cv2.waitKey(0)
    cv2.destroyAllWindows() #Close python windows
    cap.release() #Stop using camera


def liveThresh():
    print("Live thresholding")
    print("Press esc to escape the live thresholding.")
    cap = cv2.VideoCapture(0)
    while(True):
        _, frame = cap.read() #Getting frame image from live feed

        grayscaled = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 255, 32)
        cv2.imshow('Original input',frame)
        cv2.imshow('Gaussian thresholding active', gaus)

        k = cv2.waitKey(5) & 0xFF #Press Esc to close
        if k == 27:
            break

    cv2.destroyAllWindows() #Close python windows
    cap.release() #Stop using camera


if (__name__ == "__main__"):
    parser = argparse.ArgumentParser(description='Recieve images or peform live')

    parser.add_argument('-l', '--live', action="store_true",
                    help='Do the Gaussian Thresholding live')
    parser.add_argument('-i', '--image',
                    help='image which will be inputted if not live')
    args = parser.parse_args()

    if (args.live):
        liveThresh()
    else:
        if (exists(args.image)):
            print("Performing gaussian thresholding on image given")
            gaussian(image)
        else:
            print("Image specified does not exist.")

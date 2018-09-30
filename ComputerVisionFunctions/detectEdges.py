try:
    import cv2
    import numpy as np
    import argparse
    import os
    import cv2
    import numpy as np
    import time
except:
    print("Necessary packages are not imported.")
    print("Refer to requirements for necessary packages")
    sys.exit()



def exists(image):
    if (os.path.exists(os.path.join(os.getcwd(),image))):
        return True
    else:
        return False


def edges(image):
    print("Performing edge detection on given image")
    print("Press any key to close the image")


    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray, 100,200)

    cv2.imshow("Edges", edges)
    cv2.imshow("original image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def liveEdge():
    #Getting live feed
    cv2.namedWindow("face detection activated")
    vc = cv2.VideoCapture(0)

    # Try to get the first frame
    if vc.isOpened():
        rval, frame = vc.read()
    else:
        rval = False

    # Keep the video stream open
    while rval:
        # Get the image from camera, convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        # Get the edges
        edges = cv2.Canny(gray, 100,200)

        # Show both the original frame and the edges we detected from it
        cv2.imshow("Original image", frame)
        cv2.imshow("Edge detected", edges)

        # Just stuff for closing the image once you are done.
        key = cv2.waitKey(20)
        if key > 0: # Exit by pressing any key
            # Destroy windows
            cv2.destroyAllWindows()

            # Make sure window closes on OSx
            for i in range (1,5):
                cv2.waitKey(1)
            return

        # Read next frame
        time.sleep(0.05)             # control framerate for computation - default 20 frames per sec
        rval, frame = vc.read()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Recieve images or perform live')

    parser.add_argument('-l', '--live', action="store_true",
                    help='Do the edge detection live')
    parser.add_argument('-i', '--image',
                    help='image which will be inputted if not live')
    args = parser.parse_args()

    if (args.live):
        liveEdge()
    else:
        if (exists(args.image)):
            print("Performing edge detection on image given")
            edges(image)
        else:
            print("Image specified does not exist.")

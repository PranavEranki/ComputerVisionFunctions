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


def blur(image):
    print("Performing blurring of all faces on image given")
    print("Press any key to close the image")

    image_rgb = image
    image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    if (exists('haarcascade_frontalface_default.xml')):
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    else:
        print("Please download the frontalface haarcascade classifier and save it in the working dir before execution")
        sys.exit()

    faces = face_cascade.detectMultiScale(image_gray, 1.4, 6)

    # This is a kernel which will blur the face. Basically makes the value extremely close to black / gray
    kernel = np.ones((60,60), np.float32)/3600

    for (x,y,w,h) in faces:
        image_rgb[y:y+h, x:x+w, :] = cv2.filter2D(image_rgb[y:y+h, x:x+w, :], -1, kernel)

    print("Hidden identity image shown. Press any key to close.")
    cv2.imshow("identity hidden", image_rgb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def liveBlurring():
    cv2.namedWindow("face detection activated")
    vc = cv2.VideoCapture(0)

    # Try to get the first frame
    if vc.isOpened():
        rval, frame = vc.read()
    else:
        rval = False

    # Keep video stream open
    while rval:
        # Plot image from camera with detections marked
        image_copy =  np.copy(frame)

        # Convert the image to RGB colorspace to then convert into a grayscale
        # Convert the RGB  image to grayscale
        image_gray = cv2.cvtColor(image_copy, cv2.COLOR_RGB2GRAY)

        # Extract the pre-trained face detector from an xml file
        if (exists('haarcascade_frontalface_default.xml')):
            face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        else:
            print("Please download the frontalface haarcascade classifier and save it in the working dir before execution")
            sys.exit()

        # Detect the faces in image
        faces = face_cascade.detectMultiScale(image_gray, 1.4, 6)

        # This is a kernel which will blur the face. Basically makes the value extremely close to black / gray
        kernel = np.ones((60,60), np.float32)/3600

        for (x,y,w,h) in faces:
            image_rgb[y:y+h, x:x+w, :] = cv2.filter2D(image_rgb[y:y+h, x:x+w, :], -1, kernel)

        cv2.imshow("identity hidden", image_rgb)

        # Exit functionality - press any key to exit laptop video
        key = cv2.waitKey(20)
        if key > 0: # Exit by pressing any key
            # Destroy windows
            cv2.destroyAllWindows()

            for i in range (1,5):
                cv2.waitKey(1)
            return

        # Read next frame
        time.sleep(0.05)             # control framerate for computation - default 20 frames per sec
        rval, frame = vc.read()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Recieve images or perform live')

    parser.add_argument('-l', '--live', action="store_true",
                    help='Do the facial blurring live')
    parser.add_argument('-i', '--image',
                    help='image which will be inputted if not live')
    args = parser.parse_args()

    if (args.live):
        liveBlurring()
    else:
        if (exists(args.image)):
            print("Performing blurring on image given")
            blur(image)
        else:
            print("Image specified does not exist.")

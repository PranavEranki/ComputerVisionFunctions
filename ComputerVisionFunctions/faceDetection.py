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

def faces(image):
    if (exists('haarcascade_frontalface_default.xml')):
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    else:
        print("Please download the frontalface haarcascade classifier and save it in the working dir before execution")
        sys.exit()

    print("Performing face detection on given image")
    print("Press any key to close the image")

    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    face_cascade = cv2.CascadeClassifier('detector_architectures/haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.25, 6)
    image_with_detections = np.copy(image)


    for (x,y,w,h) in faces:
        # Add a red bounding box to the detections image
        cv2.rectangle(image_with_detections, (x,y), (x+w,y+h), (255,0,0), 3)

    cv2.imshow("Original", frame)
    cv2.imshow("Face Detection Activated", image_with_detections)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def liveFaces():
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
        if (exists('haarcascade_frontalface_default.xml')):
            face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        else:
            print("Please download the frontalface haarcascade classifier and save it in the working dir before execution")
            sys.exit()

        print("Performing face detection on live input")
        print("Press any key to close the live feed")

        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        face_cascade = cv2.CascadeClassifier('detector_architectures/haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray, 1.25, 6)
        image_with_detections = np.copy(frame)


        for (x,y,w,h) in faces:
            # Add a red bounding box to the detections image
            cv2.rectangle(image_with_detections, (x,y), (x+w,y+h), (255,0,0), 3)

        cv2.imshow("Original", frame)
        cv2.imshow("Face Detection Activated", image_with_detections)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


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
                    help='Do the face detection live')
    parser.add_argument('-i', '--image',
                    help='image which will be inputted if not live')
    args = parser.parse_args()

    if (args.live):
        liveFaces()
    else:
        if (exists(args.image)):
            print("Performing face detection on image given")
            faces(image)
        else:
            print("Image specified does not exist.")

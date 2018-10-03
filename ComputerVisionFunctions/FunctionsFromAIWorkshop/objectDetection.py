try:
    import cv2
    import sys
    import os
    from objectDetectionUtil import detect_common_objects, draw_bbox
    import argparse
    import time
except:
    print("Necessary packages not installed")
    sys.exit()

def exists(image):
    if (os.path.exists(os.path.join(os.getcwd(),image))):
        return True
    else:
        return False

def detect(image):
    bbox, label, conf = detect_common_objects(image)
    out = draw_bbox(image, bbox, label, conf)

    cv2.imshow("object detection", out)
    cv2.imshow("original", image)
    cv2.waitKey()
    cv2.destroyAllWindows()

def live():
    print("Live detection of objects")
    print("Press esc to escape the live detection.")
    cap = cv2.VideoCapture(0)
    while(True):
        rval, frame = cap.read() #Getting frame image from live feed
        while rval:
            bbox, label, conf = detect_common_objects(frame)
            out = draw_bbox(frame, bbox, label, conf)

            cv2.imshow("object detection", out)

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
            rval, frame = cap.read()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Recieve images or perform live')

    parser.add_argument('-l', '--live', action="store_true",
                    help='Do the face detection live')
    parser.add_argument('-i', '--image',
                    help='image which will be inputted if not live')
    args = parser.parse_args()

    if (args.live):
        live()
    else:
        if (exists(args.image)):
            print("Performing object detection on image given")
            detect(image)
        else:
            print("Image specified does not exist.")

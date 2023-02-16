# detect color of mnm based on camera input, returns colorname

# libraries
import cv2
import numpy as np

# returns colorname of mnm in camera visual
def classifier():
    # initialize the camera
    cap = cv2.VideoCapture(0)

    # set the color range for each M&M color
    color_range = {
        "red": [(0, 70, 50), (10, 255, 255)],
        "orange": [(5, 70, 50), (15, 255, 255)],
        "yellow": [(20, 70, 50), (30, 255, 255)],
        "green": [(50, 70, 50), (70, 255, 255)],
        "blue": [(100, 70, 50), (130, 255, 255)],
        "brown": [(0, 70, 20), (20, 255, 70)]
    }

    # main program loop
    while True:
        # get a frame from the camera
        ret, frame = cap.read()

        # convert the frame to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # threshold the image to get the color regions
        for color in color_range.keys():
            lower = np.array(color_range[color][0], dtype=np.uint8)
            upper = np.array(color_range[color][1], dtype=np.uint8)
            mask = cv2.inRange(hsv, lower, upper)
            # find the contours of the color regions
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            # draw the contours on the original frame
            cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
            # print the color name and number of contours found
            print(f"{color}: {len(contours)}")
            return f"{color}: {len(contours)}"

        # show the resulting frame
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

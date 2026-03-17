import numpy as np
import cv2

def get_limits(color):  

    c = np.uint8([[color]])   # here insert the bgr values which you want to convert to hsv
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    hue = hsvC[0][0][0]

    # Special case for black
    if color == [0, 0, 0]:
        lowerLimit = np.array([0, 0, 0], dtype=np.uint8)
        upperLimit = np.array([180, 255, 50], dtype=np.uint8)
    else:
        lowerHue = max(hue - 10, 0)
        upperHue = min(hue + 10, 179)

        lowerLimit = np.array([lowerHue, 100, 100], dtype=np.uint8)
        upperLimit = np.array([upperHue, 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit



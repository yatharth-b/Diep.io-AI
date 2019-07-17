import cv2
import numpy as np
from PIL import ImageGrab
from pyautogui import moveTo

template = cv2.imread('grey square1.png', 0)


while True:
    screen = np.array(ImageGrab.grab())
    img_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0], top_left[1])
    threshold = 0.65
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_gray, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
        print('square')
        print(pt[0], pt[1])
        moveTo(pt[0], pt[1])



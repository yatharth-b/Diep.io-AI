import cv2
import numpy as np
from PIL import ImageGrab
import time
import pyautogui


def search_for_squares(img):
    template = cv2.imread('grey square1.png', 0)
    cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    threshold2 = 0.45
    loc = np.where(res >= threshold2)
    if len(loc[0]) != 0:
        for pt in zip(*loc[::-1]):
            return pt[0], pt[1]


last_time = time.time()
while True:
    screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
    cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    print('That took {} seconds'.format(time.time()-last_time))
    last_time = time.time()
    search_for_squares(screen)
    cv2.imshow('window', screen)
    if cv2.waitKey(25) and 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
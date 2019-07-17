import pyautogui
from random import choice
import pickle
import time
from PIL import ImageGrab
import numpy as np
import cv2


def Intelligent_keys(loc):
    for pt in zip(*loc[::-1]):
        pyautogui.moveTo(pt[0], pt[1])


pickle_in = open('Square_hitting_data_large_and_dumb.pickle', 'rb')
Square_hit_data = pickle.load(pickle_in)
pickle_in.close()
template = cv2.imread('grey square1.png', 0)
template2 = cv2.imread('grey triangle.png', 0)
w, h = template.shape[::-1]
x = 4
go = input('enter:')
for i in range(4):
    print(x)
    time.sleep(1)
    x -= 1
print('Executing!')
pyautogui.click(773, 1051)
pyautogui.hotkey('F11')
random_key = ['w', 'a', 's', 'd']

pyautogui.hotkey('enter')
pyautogui.hotkey('enter')
pyautogui.hotkey('e')
while True:
    screen = np.array(ImageGrab.grab())
    img_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    cv2.imshow('window', img_gray)
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshhold = 0.69
    loc = np.where(res >= threshhold)
    if len(loc[0]) != 0:
        Intelligent_keys(loc)
    name_box = pyautogui.locateOnScreen('name box.png', confidence=0.7)
    res = cv2.matchTemplate(img_gray, template2, cv2.TM_CCOEFF_NORMED)
    threshold2 = 0.45
    loc2 = np.where(res >= threshold2)
    if len(loc[0]) != 0:
        for pt in zip(*loc2[::-1]):
            Intelligent_keys(loc2)
    if len(loc2[0]) == 0 and len(loc[0]) == 0:
        x = choice(random_key)
        y = choice(random_key)
        z = choice(random_key)
        a = choice(random_key)
        pyautogui.keyDown(x, 4)
        pyautogui.keyDown(y, 5)
        pyautogui.keyDown(z, 3)
        pyautogui.keyDown(a, 2)
        pyautogui.keyUp(x)
        pyautogui.keyUp(y)
        pyautogui.keyUp(z)
        pyautogui.keyUp(a)
    upgrade_button_1 = pyautogui.locateOnScreen('Upgrade1.png', confidence=0.7)
    if upgrade_button_1 is not None:
        pyautogui.moveTo(120, 175)
        pyautogui.click()
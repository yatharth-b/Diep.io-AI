import pyautogui
from random import choice
import time
x = 4
go = input('enter:')
for i in range(4):
    print(x)
    time.sleep(1)
    x -= 1
pyautogui.click(773, 1051)
random_key = ['w', 'a', 's', 'd']

pyautogui.hotkey('enter')
pyautogui.hotkey('enter')
pyautogui.hotkey('e')
while True:
    name_box = pyautogui.locateOnScreen('name box.png', confidence=0.7)
    if name_box is None:
        square1 = pyautogui.locateAllOnScreen('square1.png', confidence=0.7)
        square = list(square1)
        print(len(square))
        if len(square) != 0:
            for i in square:
                pyautogui.moveTo(pyautogui.center(i))
        else:
            x = choice(random_key)
            y = choice(random_key)
            z = choice(random_key)
            a = choice(random_key)
            pyautogui.keyDown(x, 2)
            pyautogui.keyDown(y, 2)
            pyautogui.keyDown(z, 3)
            pyautogui.keyDown(a, 2)
            pyautogui.keyUp(x)
            pyautogui.keyUp(y)
            pyautogui.keyUp(z)
            pyautogui.keyUp(a)
    else:
        pyautogui.hotkey('enter')
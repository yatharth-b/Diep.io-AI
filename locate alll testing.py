import pyautogui
from random import choice
import time

x = 4
go = input('enter:')
for i in range(4):
    print(x)
    time.sleep(1)
    x -= 1
print('Executing!')
pyautogui.click(773, 1051)
random_key = ['w', 'a', 's', 'd']

pyautogui.hotkey('enter')
pyautogui.hotkey('enter')
pyautogui.hotkey('e')
while True:
    sq = pyautogui.locateAllOnScreen('square1.png', confidence=0.5)
    sq = list(sq)
    for i in range(0, len(sq), 25):
        pyautogui.moveTo(pyautogui.center(sq[i]))
        #pyautogui.moveTo(pyautogui.center(i))
    if len(sq) == 0:
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
import pyautogui
from runbot2 import pentagon
from runbot3 import triangle1
from runbot4 import square1
from random import choice

print(pyautogui.position())
random_key = ['w', 'a', 's', 'd']
while True:
    upgrade_button_1 = pyautogui.locateOnScreen('Upgrade1.png', confidence=0.8)
    if triangle1 is None and square1 is None and pentagon is None:
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
    else:
        pyautogui.hotkey('enter')



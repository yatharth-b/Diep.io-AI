import pyautogui

triangle1 = pyautogui.locateAllOnScreen('triangle1.png', confidence=0.7)
triangle = list(triangle1)

if len(triangle) != 0:
    for i in triangle:
        pyautogui.moveTo(pyautogui.center(i))
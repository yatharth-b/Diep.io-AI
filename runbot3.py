import pyautogui
take = input('4:')
if take.lower() == 'go':
    while True:
        triangle1 = pyautogui.locateOnScreen('triangle1.png', confidence=0.6)
        if triangle1 is not None:
            center_triangle = pyautogui.center(triangle1)
            pyautogui.moveTo(center_triangle.x, center_triangle.y, 0.55)


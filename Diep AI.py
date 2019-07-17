import numpy as np
from PIL import ImageGrab
import cv2

print(ord('a'))
def process_image(original_image):
    processed_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_image = cv2.Canny(processed_image, threshold1=200, threshold2=300)
    return processed_image


def screen_record():
    while True:
        print_screen = np.array(ImageGrab.grab())
        print_screen = process_image(print_screen)
        cv2.imshow('window', cv2.cvtColor(print_screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


screen_record()
import win32api as wapi
import time as time
import cv2
import numpy as np
from PIL import ImageGrab
import os
from Grabscreen import grab_screen

#template = cv2.imread('grey square1.png', 0)
#w, h = template.shape[::-1]
keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'£$/\\":
    keyList.append(char)

filename = 'Training data.npy'

if os.path.isfile(filename):
    print('data found, loading data.')
    training_data = list(np.load(filename, allow_pickle=True))
else:
    print('File does not exist, creating a new list!')
    training_data = []
key_press_dictionary = {}


def keys_to_output(keys):
    output = [0, 0, 0, 0]
    if 'W' in keys:
        output[1] = 1
    if 'A' in keys:
        output[0] = 1
    if 'S' in keys:
        output[2] = 1
    if 'D' in keys:
        output[3] = 1

    return output


def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    return keys


s = input(' e:')
x = 4
for i in range(4):
    print(x)
    time.sleep(1)
    x -= 1
print('Executing!')

last_time = time.time()
while True:
    screen = grab_screen(region=(0, 90, 830, 520))
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    screen = cv2.resize(screen, (166, 104))
    #res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    #threshold = 0.65
    #loc = np.where(res >= threshold)
    #for pt in zip(*loc[::-1]):
    #    cv2.rectangle(img_gray, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
    keys = key_check()
    output = keys_to_output(keys)
    training_data.append([screen, output])
    print(len(training_data), output)
    if len(training_data) % 10000 == 0:
        print(len(training_data), 'done')
        np.save(filename, training_data)
    print('That took {} seconds.'.format(time.time()-last_time))
    last_time = time.time()
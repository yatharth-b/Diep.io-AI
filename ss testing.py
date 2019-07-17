from numpy import load
import pandas as pd
from collections import Counter
from random import shuffle
import cv2

training_data = load('Training data.npy', allow_pickle=True)

df = pd.DataFrame(training_data)
print(len(training_data))
print(df.head())
print(Counter(df[1].apply(str)))

#for data in training_data:
#    img = data[0]
#    choice = data[1]
#    cv2.imshow('window', img)
#    print(choice)
#    if cv2.waitKey(25) & 0xFF == ord('q'):
#        cv2.destroyAllWindows()
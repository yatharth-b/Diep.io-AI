import numpy as np

training_data = np.load('Training data.npy', allow_pickle=True)
training_data = list(training_data)
x = 0
for i in training_data:
    if i[1] == [0, 0, 0, 0]:
        del training_data[x]
    x += 1

np.save('Training data.npy', training_data)
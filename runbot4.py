import pickle
for k in range(4):
    pickle_in = open('Square_hitting_data_large_and_dumb.pickle', 'rb')
    dict = pickle.load(pickle_in)
    pickle_in.close()

    pickle_in_2 = open('Square_hitting_data_large_and_dumb.pickle', 'rb')
    dict_copy = pickle.load(pickle_in_2)
    pickle_in_2.close()
    for pixel in dict_copy:
        for i in range(100):
            dict[(pixel[0] + i, pixel[1] + i)] = dict[pixel]
            if pixel[0] >= 100 and pixel[1] >= 100:
                dict[(pixel[0] - i, pixel[1] - i)] = dict[pixel]
    pickle_out = open('Square_hitting_data_large_and_dumb.pickle', 'wb')
    pickle.dump(dict, pickle_out)
    pickle_out.close()

    print(len(dict))
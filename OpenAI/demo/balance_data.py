# Developed by Chris Liu
import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2

# w = [1, 0, 0, 0, 0, 0, 0, 0, 0]
# s = [0, 1, 0, 0, 0, 0, 0, 0, 0]
# a = [0, 0, 1, 0, 0, 0, 0, 0, 0]
# d = [0, 0, 0, 1, 0, 0, 0, 0, 0]
# wa = [0, 0, 0, 0, 1, 0, 0, 0, 0]
# wd = [0, 0, 0, 0, 0, 1, 0, 0, 0]
# sa = [0, 0, 0, 0, 0, 0, 1, 0, 0]
# sd = [0, 0, 0, 0, 0, 0, 0, 1, 0]

train_data = np.load('training_data-1.npy', allow_pickle=True)
# for data in train_data:
#     img = data[0]
#     choice = data[1]
#     cv2.imshow('test', img)
#     print(choice)
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()
#         break
df = pd.DataFrame(train_data)
print(df.head())
print(Counter(df[1].apply(str)))

lefts = []
rights = []
ups = []
downs = []
# # left_ups = []
# # right_ups = []
# # left_downs = []
# # right_downs = []
#
shuffle(train_data)

for data in train_data:
    img = data[0]
    choice = data[1]

#     # if choice == [1, 0, 0, 0, 0, 0, 0, 0, 0]:
#     #     ups.append([img, choice])
#     # elif choice == [0, 1, 0, 0, 0, 0, 0, 0, 0]:
#     #     downs.append([img, choice])
#     # elif choice == [0, 0, 0, 1, 0, 0, 0, 0, 0]:
#     #     rights.append([img, choice])
#     # elif choice == [0, 0, 1, 0, 0, 0, 0, 0, 0]:
#     #     lefts.append([img, choice])
#     # elif choice == [0, 0, 0, 0, 1, 0, 0, 0, 0]:
#     #     left_ups.append([img, choice])
#     # elif choice == [0, 0, 0, 0, 0, 1, 0, 0, 0]:
#     #     right_ups.append([img, choice])
#     # elif choice == [0, 0, 0, 0, 0, 0, 1, 0, 0]:
#     #     left_downs.append([img, choice])
#     # elif choice == [0, 0, 0, 0, 0, 0, 0, 1, 0]:
#     #     right_downs.append([img, choice])
    if choice == [1, 0, 0, 0]:
        ups.append([img, choice])
    elif choice == [0, 1, 0, 0]:
        downs.append([img, choice])
    elif choice == [0, 0, 0, 1]:
        rights.append([img, choice])
    elif choice == [0, 0, 1, 0]:
        lefts.append([img, choice])
    else:
        print('no matches')

rights = rights[:len(ups)][:len(downs)]
ups = ups[:len(rights)]
lefts = lefts[:len(rights)]
downs = downs[:len(rights)]

final_data = rights + lefts + ups + downs
shuffle(final_data)

np.save('training_data-final.npy', final_data)

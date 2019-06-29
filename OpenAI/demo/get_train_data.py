# Developed by Chris Liu
import numpy as np
from OpenAI.demo.screenshot import screenshot
import cv2
import time
from OpenAI.demo.get_key import key_check
import os

# w = [1, 0, 0, 0, 0, 0, 0, 0, 0]
# s = [0, 1, 0, 0, 0, 0, 0, 0, 0]
# a = [0, 0, 1, 0, 0, 0, 0, 0, 0]
# d = [0, 0, 0, 1, 0, 0, 0, 0, 0]
# wa = [0, 0, 0, 0, 1, 0, 0, 0, 0]
# wd = [0, 0, 0, 0, 0, 1, 0, 0, 0]
# sa = [0, 0, 0, 0, 0, 0, 1, 0, 0]
# sd = [0, 0, 0, 0, 0, 0, 0, 1, 0]
w = [1, 0, 0, 0]
s = [0, 1, 0, 0]
a = [0, 0, 1, 0]
d = [0, 0, 0, 1]

starting_value = 1


def keys_to_output(keys):
    '''
    Convert keys to a ...multi-hot... array
     0  1  2  3  4   5   6   7    8
    [W, S, A, D, WA, WD, SA, SD, NOKEY] boolean values.
    '''
    # output = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    output = [0, 0, 0, 0]
    # if 'W' in keys and 'A' in keys:
    #     output = wa
    # elif 'W' in keys and 'D' in keys:
    #     output = wd
    # elif 'S' in keys and 'A' in keys:
    #     output = sa
    # elif 'S' in keys and 'D' in keys:
    #     output = sd
    if 'W' in keys:
        output = w
    elif 'S' in keys:
        output = s
    elif 'A' in keys:
        output = a
    elif 'D' in keys:
        output = d
    return output


def main(file_name, starting_value):
    file_name = file_name
    starting_value = starting_value
    training_data = []
    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)

    # last_time = time.time()
    paused = False
    print('STARTING!!!')
    while True:

        if not paused:
            screen = np.array(screenshot())
            # last_time = time.time()
            # resize to something a bit more acceptable for a CNN
            # screen = cv2.resize(screen, (480, 270))
            # run a color convert:
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (160, 90))
            keys = key_check()
            output = keys_to_output(keys)
            training_data.append([screen, output])

            # print('loop took {} seconds'.format(time.time()-last_time))
            # last_time = time.time()
            ##            cv2.imshow('window',cv2.resize(screen,(640,360)))
            ##            if cv2.waitKey(25) & 0xFF == ord('q'):
            ##                cv2.destroyAllWindows()
            ##                break

            if len(training_data) % 100 == 0:
                print(len(training_data))

                if len(training_data) == 500:
                    np.save(file_name, training_data)
                    print('SAVED')
                    training_data = []
                    starting_value += 1
                    file_name = f'training_data-{starting_value}.npy'

        keys = key_check()
        if 'T' in keys:
            if paused:
                paused = False
                print('unpaused!')
                time.sleep(1)
            else:
                print('Pausing!')
                paused = True
                time.sleep(1)


def record():
    main(file_name, starting_value)


if __name__ == '__main__':
    while True:
        file_name = 'training_data-{}.npy'.format(starting_value)

        if os.path.isfile(file_name):
            print('File exists, moving along', starting_value)
            starting_value += 1
        else:
            print('File does not exist, starting fresh!', starting_value)
            break
    record()

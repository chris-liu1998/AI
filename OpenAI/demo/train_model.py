# Developed by Chris Liu
import numpy as np
from OpenAI.demo.Cnn_model import alexnet
import warnings

warnings.filterwarnings("ignore")

WIDTH = 160
HEIGHT = 90
LR = 1e-3
EPOCHS = 10
MODEL_NAME = 'pygta5-car-fast-{}-{}-{}-epochs-300K-data.model'.format(LR, 'alexnetv2', EPOCHS)

model = alexnet(WIDTH, HEIGHT, LR)

hm_data = 22
for i in range(EPOCHS):
    for i in range(1, hm_data + 1):
        train_data = np.load('training_data-1.npy', allow_pickle=True)
        train = train_data[:184]
        test = train_data[184:]

        X = np.array(([i[0] for i in train])).reshape([-1, WIDTH, HEIGHT, 1])
        Y = [i[1] for i in train]

        test_x = np.array(([i[0] for i in train])).reshape([-1, WIDTH, HEIGHT, 1])
        test_y = [i[1] for i in test]

        model.fit({'input': X}, {'targets': Y}, n_epoch=1, validation_set=({'input': test_x}, {'targets': test_y}),
                  snapshot_step=500, show_metric=True, run_id=MODEL_NAME)

        model.save(MODEL_NAME)

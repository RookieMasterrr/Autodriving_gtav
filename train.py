import numpy as np
from pilotNet import pilotnet

def train_model(train_data):
    WIDTH=160
    HEIGHT=120
    LR=1e-3
    EPOCHS=50
    MODEL_NAME='pygta5-car-{}-{}-{}-epochs.model'.format(LR,'pilotnet',EPOCHS)

    model = pilotnet(WIDTH,HEIGHT,LR)


    np.random.shuffle(train_data)

    testsise=(int)(len(train_data)/5)

    train = train_data[:-testsise]
    test = train_data[-testsise:]

    X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
    Y = [i[1] for i in train]

    test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
    test_y = [i[1] for i in test]

    model.fit({'input': X}, {'targets': Y}, n_epoch=EPOCHS, validation_set=({'input': test_x}, {'targets': test_y}), 
        snapshot_step=100, show_metric=True, run_id=MODEL_NAME)

    model.save(MODEL_NAME)
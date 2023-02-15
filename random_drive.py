import time
import numpy as np
from vjoy import *
data=np.load('train_data.npy',allow_pickle=True)

vj.open()

def steer(orit):
    setJoy(orit[0],orit[1])
    vj.setButton(5,orit[2])
    

for i in range(0,4):
    time.sleep(1)
    print(i)

for d in data:
    print(d[1])
    steer(d[1])

vj.close()
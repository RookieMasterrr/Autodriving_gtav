from copy import copy
from re import I
import time
import numpy as np
import cv2


def showimg(screen):
    cv2.imshow('screen',screen)


def flip(l):
    l[1]=-l[1]
    return l

datas = np.load('large_data_with_balance.npy',allow_pickle=True)

newdatas = np.load('large_data_with_balance_filped.npy',allow_pickle=True)

# newdatas=datas.copy()

# for d in newdatas:
#     d[0]=(cv2.flip(d[0],1))
#     d[1] = flip(d[1])


# count=0
# while(True):
#     time.sleep(1)
#     cv2.imshow('1',datas[count][0])
#     print(datas[count][1][1])

#     cv2.imshow('2',newdatas[count][0])
#     print(newdatas[count][1][1])
#     count+=1
#     if cv2.waitKey(25)&0xFF==27:
#         cv2.destroyAllWindows()
#         exit(0)

# np.save('large_data_with_balance_filped.npy',newdatas)
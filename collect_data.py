# before collect data,disable the vjoy first to avoid the conflict
print('a real controller should work now')

import time
# get data from controller
import pygame
from pygame.locals import *
# get img
from grabscreen import grab_screen
#process img
import cv2
import numpy as np
import os

# pre-info
pygame.init()
pygame.joystick.init()
joystick_num = pygame.joystick.get_count()
print('{} joysticks is available'.format(joystick_num))
mystick=pygame.joystick.Joystick(0)
# for i in range(0,joystick_num):
#     stick = pygame.joystick.Joystick(i)
#     if stick.get_guid()=="030000005e040000ff02000000007200":
#         mystick = stick
#         print("device {} is found and id is {}".format(mystick.get_name(),mystick.get_id()))
#         break

mystick.init()
# print('{} axis exist'.format(mystick.get_numaxes()))

# axis=5 forward range from -1(full stop)~1(full acc)
# axis=0 left or right from -1(full left)~0(whell stay)~1(full right)

# load train_file
# file_name='new_train_data.npy'



def showimg(screen):
    cv2.imshow('screen',screen)
    if cv2.waitKey(25)&0xFF==27:
        cv2.destroyAllWindows()



for i in range(0,5):
    print('get in the car')
    print(i)
    time.sleep(1)





for i in range(9,20):
    file_name='new_train_data_{}.npy'.format(i)
    train_data=[]

    while True:
        # 截取图片
        screen = grab_screen(region=(0,40,800,620))
        screen = cv2.resize(screen,(160,120))
        # 转化成灰度图片
        screen = cv2.cvtColor(screen,cv2.COLOR_BGR2GRAY)

        # showimg(screen)

        # 使用pygame.joystick库获取实体手柄的输入
        pygame.event.pump()
        if mystick.get_button(0)==1:#按A以停止收集
            exit(0)
        output = [mystick.get_axis(5),mystick.get_axis(0)]#收集油门+收集转向

        # 添加到训练集中
        train_data.append([screen,output])

        # 控制每次收集的文件的大小避免程序阻塞以错过一些数据
        if len(train_data) % 500 == 0:
            print(len(train_data))
            np.save(file_name,train_data)
        if len(train_data)==10000:
            print('file_{}'.format(i,)+'loaded')
            break
        
from concurrent.futures import thread
import threading
import sys
from charset_normalizer import detect
from keras.models import load_model
from genericpath import isfile
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
from pilotNet import pilotnet
from vjoy import *
from YoloWithGame import analyzeTheImg


vj.open()

def steer(orit):

    if orit[1]>0:
        orit[1]+=0.15
    else:
        orit[1]-=0.15

    if tooClose==0:
        setJoyAndBtd(orit[0],orit[1],0)
    else:
        setJoyAndBtd(-1,orit[1],0)

WIDTH=160
HEIGHT=120
LR=1e-3
EPOCHS=50
MODEL_NAME='pygta5-car-{}-{}-{}-epochs.model'.format(LR,'pilotnet',EPOCHS)
model = pilotnet(WIDTH,HEIGHT,LR)
model.load(MODEL_NAME)


def detectInput2Stop():
    while True:
        a=input()
        if (a=='q' or a=='Q'):
            steer([-1,0])
            os._exit(0)



#导入YOLO
# net = cv2.dnn.readNet("yolov3-tiny.weights", "yolov3-tiny.cfg")
# classes = []

# with open("coco.names.txt", "r") as f:
#     classes = [line.strip() for line in f.readlines()]
# layer_names = net.getLayerNames()




# for i in range(0,3):
#     print('get in the car')
#     print(i)
#     time.sleep(1)


img:np.ndarray
tooClose=0

def analyzeTheGameImgWithYolo():
    global tooClose
    while(True):
        processedImg,tooClose = analyzeTheImg(img)
        cv2.imshow("img",processedImg)
        cv2.waitKey(1)& 0xFF == ord('q')


def run():
    global img
    while True:
        # get img input

        begin=time.time()

        screen = grab_screen(region=(0,40,800,620))
        img = screen
        # img = screen[0:450,200:600]
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

        screen = cv2.resize(screen,(160,120))
        screen = cv2.cvtColor(screen,cv2.COLOR_BGR2GRAY)

        pred = model.predict([screen.reshape(WIDTH,HEIGHT,1)])[0]

        print(pred,end="")
        steer(pred)
        
        after=time.time()
        gap=after-begin
        print(str(1/gap)+" frame/s")


t1=threading.Thread(target=run)
t2=threading.Thread(target=detectInput2Stop)
# t3=threading.Thread(target=analyzeTheGameImgWithYolo)

t1.start()
t2.start()
# time.sleep(1)
# t3.start()
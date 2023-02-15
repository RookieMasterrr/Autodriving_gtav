import pygame
from pygame.locals import *
pygame.init()
pygame.joystick.init()

mystick = pygame.joystick.Joystick(0)

mystick.init()

while True:
    pygame.event.pump()
    # print(mystick.get_axis(5))#油门
    print(mystick.get_axis(0))#左右 小于|0.07|说明无效
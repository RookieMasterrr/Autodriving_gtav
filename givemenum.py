import pygame
from pygame.locals import *


pygame.init()


num = pygame.joystick.get_count()


for i in range(0,num):
    stick = pygame.joystick.Joystick(i)
    print(stick.get_name()+"  "+str(stick.get_id()))
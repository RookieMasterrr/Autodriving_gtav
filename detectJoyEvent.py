import pygame
from pygame.locals import *
pygame.init()
pygame.joystick.init()

mystick = pygame.joystick.Joystick(0)

while True:
    for event in pygame.event.get():
        print(event)
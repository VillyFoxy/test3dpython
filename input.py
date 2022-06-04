import pygame
from settings import *
def push(but):
    KEYS = pygame.mouse.get_pressed()
    MOUSE = pygame.mouse.get_pos()
    if but.x < MOUSE[0] < but.x + but.w:
        if but.y < MOUSE[1] < but.y + but.h:
            if KEYS[0] == 1:
                return True
def inputs():
    if push(UP):
        ANDROID_BUTTONS['front'] = True
        ANDROID_BUTTONS['back'] = False
        ANDROID_BUTTONS['right'] = False
        ANDROID_BUTTONS['left'] = False
    elif push(DOWN):
        ANDROID_BUTTONS['back'] = True
        ANDROID_BUTTONS['front'] = False
        ANDROID_BUTTONS['right'] = False
        ANDROID_BUTTONS['left'] = False
    elif push(RIGHT):
        ANDROID_BUTTONS['right'] = True
        ANDROID_BUTTONS['front'] = False
        ANDROID_BUTTONS['back'] = False
        ANDROID_BUTTONS['left'] = False
    elif push(LEFT):
        ANDROID_BUTTONS['left'] = True
        ANDROID_BUTTONS['front'] = False
        ANDROID_BUTTONS['back'] = False
        ANDROID_BUTTONS['right'] = False
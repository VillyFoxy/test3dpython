import math
import pygame
# window
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
# fps
FPS = 60
FPS_POS = (WIDTH - 65, 5)
# tile
TILE = 100
# map
MAP_SCALE = 5
MAP_TILE = TILE // MAP_SCALE
MAP_POS = (0, HEIGHT - HEIGHT // MAP_SCALE)
# camera
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 300
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH // NUM_RAYS
TEXTURE_WIDTH = 1024
TEXTURE_HEIGHT = 1024
TEXTURE_SCALE = TEXTURE_WIDTH // TILE
# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 80, 0)
BLUE = (0, 0, 220)
DARKGRAY = (40, 40, 40)
PURPLE = (120, 0, 120)
SKYBLUE = (0, 186, 255)
YELLOW = (220, 220, 0)
DARKBROWN = (97, 61, 25)
DARKORANGE = (255, 140, 0)
# player
player_pos = (HALF_WIDTH // 4, HALF_HEIGHT - 50)
SANDY = (244, 164, 96)
player_angle = 0
player_speed = 2
# input
UP = pygame.Rect((150, 200), (150, 150))
DOWN = pygame.Rect((150, 550), (150, 150))
RIGHT = pygame.Rect((300, 370), (150, 150))
LEFT = pygame.Rect((0, 370), (150, 150))
ANDROID_BUTTONS = {
    'front': False,
    'back': False,
    'right': False,
    'left': False
}
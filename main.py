import pygame
from settings import *
from player import Player
import math
from map import world_map
from rendering import Rendering
from input import inputs
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
clock = pygame.time.Clock()
player = Player()
rendering = Rendering(screen, screen_map)
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
	player.movement()
	inputs()
	screen.fill(BLACK)
	rendering.background(player.angle)
	rendering.world(player.pos, player.angle)
	rendering.fps(clock)
	rendering.mini_map(player)
	rendering.buttons(screen)
	pygame.display.flip()
	clock.tick(FPS)
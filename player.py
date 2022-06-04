import pygame
from settings import *
import math
class Player:
	def __init__(self):
		self.x, self.y = player_pos
		self.angle = player_angle
	@property
	def pos(self):
		return (self.x, self.y)
	def movement(self):
		sin_a = math.sin(self.angle)
		cos_a = math.cos(self.angle)
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w] or ANDROID_BUTTONS['front']:
			self.x += player_speed * cos_a
			self.y += player_speed * sin_a
			print('W')
		if keys[pygame.K_s] or ANDROID_BUTTONS['back']:
			self.x += -player_speed * cos_a
			self.y += -player_speed * sin_a
			print('S')
		if keys[pygame.K_a] or ANDROID_BUTTONS['left']:
			self.x += player_speed * sin_a
			self.y += -player_speed * cos_a
			print('A')
		if keys[pygame.K_d] or ANDROID_BUTTONS['right']:
			self.x += -player_speed * sin_a
			self.y += player_speed * cos_a
			print('D')
		if keys[pygame.K_LEFT]:
			self.angle -= 0.02
		if keys[pygame.K_RIGHT]:
			self.angle += 0.02
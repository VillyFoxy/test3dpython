import pygame
from settings import *
from ray_casting import ray_casting
from map import mini_map
class Rendering:
    def __init__(self, screen, screen_map):
        self.screen = screen
        self.screen_map = screen_map
        self.font = pygame.font.SysFont('Arial', 35, bold = True)
        self.textures = {'1': pygame.image.load('img/1.png').convert(),
                         '2': pygame.image.load('img/2.png').convert(),
                         'S': pygame.image.load('img/sky1.png').convert()
                        }
    def background(self, angle):
        sky_offset = -10 * math.degrees(angle) % WIDTH
        self.screen.blit(self.textures['S'], (sky_offset, 0))
        self.screen.blit(self.textures['S'], (sky_offset - WIDTH, 0))
        self.screen.blit(self.textures['S'], (sky_offset + WIDTH, 0))
        pygame.draw.rect(self.screen, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))
    def world(self, player_pos, player_angle):
        ray_casting(self.screen, player_pos, player_angle, self.textures)
    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, DARKORANGE)
        self.screen.blit(render, FPS_POS)
    def mini_map(self, player):
        self.screen_map.fill(BLACK)
        map_x, map_y = player.x // MAP_SCALE, player.y // MAP_SCALE
        pygame.draw.line(self.screen_map, YELLOW, (map_x, map_y), (map_x + 12 * math.cos(player.angle),
                                                     map_y + 12 * math.sin(player.angle)))
        pygame.draw.circle(self.screen_map, RED, (int(map_x), int(map_y)), 5)
        for x, y in mini_map:
            pygame.draw.rect(self.screen_map, DARKBROWN, (x, y, MAP_TILE, MAP_TILE))
        self.screen.blit(self.screen_map, MAP_POS)
    def buttons(self, screen):
        screen.fill(RED, UP)
        screen.fill(RED, DOWN)
        screen.fill(RED, RIGHT)
        screen.fill(RED, LEFT)

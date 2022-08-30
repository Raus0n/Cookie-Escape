import pygame
from level import Level
import settings

pygame.init()

SCREEN_HEIGHT = 960
SCREEN_WIDTH = 960

screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
pygame.display.set_caption("Based Game")

level = Level(settings.level_map , screen)


running = True
while running:

    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    level.run()
    pygame.display.update()
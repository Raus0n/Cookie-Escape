import pygame
from level import Level
import settings,os

pygame.init()

SCREEN_HEIGHT = 960
SCREEN_WIDTH = 960

BLACK = (0,0,0)
WHITE = (255,255,255)

FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
pygame.display.set_caption("Based Game")

level = Level(settings.level_map , screen)

def main():
    
    
    
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()


    level.run()
    pygame.display.update()
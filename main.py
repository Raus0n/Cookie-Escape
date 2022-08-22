import pygame
from tiles import Tile

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
pygame.display.set_caption("Based Game")

tile = Tile(64 , (111 , 111))
tile_group = pygame.sprite.Group()
tile_group.add(tile)


running = True
while running:

    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    tile_group.draw(screen)
    pygame.display.update()
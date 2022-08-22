import pygame
from tiles import Tile

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
pygame.display.set_caption("Based Game")

tile_group = pygame.sprite.Group()
tile = Tile(64 , (0 , 0))
tile_group.add(tile)



running = True
while running:

    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    stripes = tile_group.sprites()
    if key[pygame.K_d]:
        for stripe in tile_group:
            stripe.x_slide = 1
    else:
        for stripe in tile_group:
            stripe.x_slide = 0

    tile_group.update()
    tile_group.draw(screen)
    pygame.display.update()
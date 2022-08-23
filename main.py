import pygame
from playerTile import PlayerTile
from tiles import Tile

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
pygame.display.set_caption("Based Game")

player_group = pygame.sprite.GroupSingle()
player = PlayerTile(64 , (111 , 111))
player_group.add(player)



running = True
while running:

    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    player_group.update()
    player_group.draw(screen)
    pygame.display.update()
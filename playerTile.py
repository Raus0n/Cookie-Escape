import pygame

from tiles import Tile

class PlayerTile(Tile):
    def __init__(self, size, pos) -> None:
        super().__init__(size, pos)


    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_s]:
            self.direction.y = 1
        elif keys[pygame.K_w]:
            self.direction.y = -1
        else:
            self.direction.y = 0
        
    def update(self):
        self.get_input()
        self.rect.x += self.direction.x
        self.rect.y += self.direction.y
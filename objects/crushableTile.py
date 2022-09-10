from multiprocessing import set_forkserver_preload
import pygame

from shapes.tiles import Tile

class CrushAbleTile(Tile):
    def __init__(self, size, pos) -> None:
        super().__init__(size, pos, "brown")
        self.image = pygame.image.load(".\\resources\\images\\crushable_tile.png")
        self.rect = self.image.get_rect(topleft = pos)

    def update(self , x_world_shift , y_world_shift):
            self.rect.x += x_world_shift
            self.rect.y += y_world_shift
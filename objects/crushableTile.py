import pygame

from shapes.tiles import Tile

class CrushAbleTile(Tile):
    def __init__(self, size, pos) -> None:
        super().__init__(size, pos, "brown")
        self.image = pygame.image.load(".\\resources\\images\\crushable_tile.png")
        self.rect = self.image.get_rect(topleft = pos)
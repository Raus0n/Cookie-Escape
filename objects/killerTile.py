import pygame

class KillerTile(pygame.sprite.Sprite):
    def __init__(self , pos) -> None:
        super().__init__()
        self.image = pygame.Surface((64 ,64))
        self.image.fill("orange")
        self.rect = self.image.get_rect(topleft = pos)

    def update(self , tile_x_shift , tile_y_shift) -> None:
        self.rect.x += tile_x_shift
        self.rect.y += tile_y_shift
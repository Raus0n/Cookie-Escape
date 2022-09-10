import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, size , pos, color) -> None:
        super().__init__()
        # self.image = pygame.Surface((size ,size))
        # self.image.fill(color)
        self.image = pygame.image.load(".\\resources\\images\\crushable_tile.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.x_slide = 2
        self.y_slide = 2

    def update(self , x_world_shift , y_world_shift):
        self.rect.x += x_world_shift
        self.rect.y += y_world_shift
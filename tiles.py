import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, size , pos) -> None:
        super().__init__()
        self.image = pygame.Surface((size ,size))
        self.image.fill("black")
        self.rect = self.image.get_rect(topleft = pos)

    def update(self):
        pass
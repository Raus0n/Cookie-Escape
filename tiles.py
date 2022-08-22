import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, size , pos) -> None:
        super().__init__()
        self.x_slide = 0
        self.y_slide = 0
        self.image = pygame.Surface((size ,size))
        self.image.fill((0 , 0 ,0))
        self.rect = self.image.get_rect(topleft = pos)

    def update(self):
        self.rect.x += self.x_slide
        self.rect.y += self.y_slide
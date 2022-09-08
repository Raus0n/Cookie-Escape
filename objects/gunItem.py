import pygame

class GunItem(pygame.sprite.Sprite):
    def __init__(self , pos):
        super().__init__()
        self.image = pygame.Surface((64 , 64))
        self.image.fill("blue")
        self.rect = self.image.get_rect(topleft = pos)

    def update(self , world_x_shift , world_y_shift):
        self.rect.x += world_x_shift
        self.rect.y += world_y_shift
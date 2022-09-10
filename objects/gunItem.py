import pygame

class GunItem(pygame.sprite.Sprite):
    def __init__(self , pos):
        super().__init__()
        self.image = pygame.image.load(".\\resources\\images\\gun_pickable.png")
        self.rect = self.image.get_rect(topleft = pos)

    def update(self , world_x_shift , world_y_shift):
        self.rect.x += world_x_shift
        self.rect.y += world_y_shift
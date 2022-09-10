import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(".\\resources\\images\\platform.png")
        self.image = pygame.transform.scale(self.image , (128 , 128))
        self.rect = self.image.get_rect(topleft = pos)

    def update(self , world_shift_x , world_shift_y):
        self.rect.x += world_shift_x
        self.rect.y += world_shift_y
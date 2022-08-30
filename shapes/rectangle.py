import pygame

class Rectnagle(pygame.sprite.Sprite):
    def __init__(self, size:list , color , pos):
        super().__init__()
        self.image = pygame.Surface((size[0] , size[1]))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft = pos)
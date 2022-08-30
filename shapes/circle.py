import pygame

class Circle(pygame.sprite.Sprite):
    def __init__(self, radius, color , transperency_color , pos):
        super().__init__()
        self.diameter = radius * 2
        self.radius = radius
        self.image = pygame.Surface((self.diameter , self.diameter))
        self.image.fill(transperency_color)
        self.image.set_colorkey(transperency_color)
        pygame.draw.circle(self.image ,color , (self.radius , self.radius) ,self.radius)
        self.rect = self.image.get_rect(center = pos)
        
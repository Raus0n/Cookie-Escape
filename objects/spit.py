import pygame
from shapes.circle import Circle

class Spit(Circle):
    def __init__(self, radius, pos):
        super().__init__(radius, "yellow", "green", pos)
        self.direction = pygame.math.Vector2(1,0)
        self.speed = 0.1

    def update(self ,world_shift_x , world_shift_y):
        self.rect.x += world_shift_x
        self.rect.y += world_shift_y
        self.rect.x += self.direction.x * self.speed
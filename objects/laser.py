import pygame

class Lazer(pygame.sprite.Sprite):
    def __init__(self , pos):
        super().__init__()
        self.image = pygame.Surface((8 , 64))
        self.image.fill("red")
        self.rect = self.image.get_rect(bottomright = pos)
        self.direction = pygame.math.Vector2(0,-1)
        self.speed = 1.5


    def update(self):
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed
        if (self.rect.x < 0 or self.rect.x > 960) or (self.rect.y < 0 or self.rect.y > 960):
            self.remove()
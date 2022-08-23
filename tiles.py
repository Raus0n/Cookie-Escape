import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, size , pos) -> None:
        super().__init__()
        self.image = pygame.Surface((size ,size))
        self.image.fill((0 , 0 ,0))
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0,0)

    def update(self):
        self.rect.x += self.direction.x
        self.rect.y += self.direction.y
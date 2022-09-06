import pygame 

class InvisibleTile(pygame.sprite.Sprite):
    def __init__(self , pos) -> None:
        super().__init__()
        self.image = pygame.Surface((64 ,64))
        self.image.fill("yellow")
        self.image.set_colorkey("yellow")
        self.rect = self.image.get_rect(topleft = pos)


    def update(self , x_world_shift , y_world_shift):
        self.rect.x += x_world_shift
        self.rect.y += y_world_shift
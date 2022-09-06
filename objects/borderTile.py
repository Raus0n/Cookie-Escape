from pydoc import classname
import pygame 
from virtualPos import VirtualPos




class BorderTile(pygame.sprite.Sprite):
    def __init__(self , pos , slide) -> None:
        super().__init__()
        self.image = pygame.Surface((64 ,64))
        self.image.fill("green")
        self.image.set_colorkey("green")
        self.rect = self.image.get_rect(topleft = pos)


    def update(self , x_world_shift , y_world_shift):
        self.rect.x += x_world_shift
        self.rect.y += y_world_shift

        


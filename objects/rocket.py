from json import load
import pygame

class Rocket(pygame.sprite.Sprite):
    def __init__(self , pos) -> None:
        super().__init__()
        self.image = pygame.image.load("./resources/images/rocket.png")
        self.image = pygame.transform.scale(self.image , (512 , 512))
        self.rect = self.image.get_rect(topleft = pos)
        print(self.rect.x , self.rect.y)
        print("load")


    def update(self , x_world_shift , y_world_shift):
        self.rect.x += x_world_shift
        self.rect.y += y_world_shift
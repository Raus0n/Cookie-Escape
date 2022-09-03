import pygame

from shapes.image import ImageSprite

class TMNFCar(ImageSprite):
    def __init__(self,pos, rotate, scale) -> None:
        super().__init__("./resources/images/tm car.png" , pos, rotate, scale)


    def update(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= 2
        if keys[pygame.K_DOWN]:
            self.rect.y += 2
        if keys[pygame.K_RIGHT]:
            self.rect.x += 2
        if keys[pygame.K_LEFT]:
            self.rect.x -= 2
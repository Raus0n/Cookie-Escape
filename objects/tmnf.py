import pygame

class TMNFCar(pygame.sprite.Sprite):
    def __init__(self , pos) -> None:
        super().__init__()
        self.image = pygame.image.load("tm car.png")
        self.image = pygame.transform.rotate(self.image , 90)
        self.image = pygame.transform.scale(self.image , (64 ,64))
        self.rect = self.image.get_rect(topleft = pos)


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
import pygame

class ImageSprite(pygame.sprite.Sprite):
    def __init__(self,image,pos,rotate,scale) -> None:
        super().__init__()
        self.image = pygame.image.load(image)
        if not rotate == None:
            self.image = pygame.transform.rotate(self.image, rotate)
        if not scale == None:
            self.image = pygame.transform.scale(self.image , scale)
        self.rect = self.image.get_rect(topleft = pos)
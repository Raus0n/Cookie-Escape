import pygame
from objects.spit import Spit 
from virtualPos import VirtualPos

class Monster(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load(".\\resources\\images\\boss.png")
        self.image = pygame.transform.scale(self.image , (256 , 256))
        self.rect = self.image.get_rect(topleft = pos)
        self.last_shot = 0
        self.spit_group = pygame.sprite.Group()
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 0.5


    def spit(self , player : pygame.sprite.Sprite):
        self.last_shot = 0
        spit = Spit(10 , (self.rect.right , self.rect.centery))
        self.spit_group.add(spit)

    def move(self , player : pygame.sprite.Sprite):
        interval = VirtualPos((player.rect.centerx - self.rect.right) ,(player.rect.centery - self.rect.centery))
        if player.rect.centery - self.rect.centery > 0:
            self.direction.y = -1
        elif    player.rect.centery - self.rect.centery > 0 :
            self.direction.y = 1
            print("gets here")
        else:
            self.direction.y = 0

    def get_spit(self):
        return self.spit_group
        
    def update(self , world_shift_x ,world_shift_y , player : pygame.sprite.Sprite):
        self.rect.y += self.direction.y * self.speed
        if self.last_shot > 3600:
            self.spit(player)

        # self.move(player)
        self.last_shot += 1
        self.rect.x += world_shift_x
        self.rect.y += world_shift_y
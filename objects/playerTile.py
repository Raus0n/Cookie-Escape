import pygame
import math
from objects.laser import Lazer

from shapes.tiles import Tile

class PlayerTile(Tile):
    def __init__(self, size, pos, color) -> None:
        super().__init__(size, pos, color)
        self.original_image = pygame.image.load("resources\\images\\player_cookie.png")
        self.image = self.original_image
        self.image = pygame.transform.scale(self.image , (96 , 96))
        self.rect = self.image.get_rect(topleft = pos)
        self.rotation = 0
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 1
        self.last_shot = 0
        self.lazers_shot = pygame.sprite.Group()
        self.armed = False



    def get_input(self):
        keys = pygame.key.get_pressed()
        if pygame.mouse.get_pressed()[0]:
            if self.last_shot > 120 and self.armed:
                print("shoot")
                self.shoot()
        
        if keys[pygame.K_UP]:
            self.rotation = 90
            self.rotate(self.rotation)
        elif keys[pygame.K_DOWN]:
            self.rotation = 270
            self.rotate(self.rotation)
        elif keys[pygame.K_RIGHT]:
            self.rotation = 0
            self.rotate(self.rotation)
        elif keys[pygame.K_LEFT]:
            self.rotation = 180
            self.rotate(self.rotation)

        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_s]:
            self.direction.y = 1
        elif keys[pygame.K_w]:
            self.direction.y = -1
        else:
            self.direction.y = 0

    def shoot(self):
        player_pos_x , player_pos_y = self.rect.center
        mouse_x , mouse_y = pygame.mouse.get_pos()
        x_interval = mouse_x - player_pos_x
        y_interval = mouse_y - player_pos_y

        rot = math.atan(y_interval / x_interval)

        print(rot)

        x = math.cos(rot)
        y = math.sin(rot)


        self.last_shot = 0
        lazer = Lazer((self.rect.right , self.rect.top))

        lazer.direction.x = x
        lazer.direction.y = y
        pygame.transform.rotate(lazer.image , self.rotation)

        self.lazers_shot.add(lazer)
        
        


    def get_lasers_shot(self) -> pygame.sprite.Group:
        return self.lazers_shot


    def rotate(self , degree):
        self.image = self.original_image
        self.image = pygame.transform.scale(self.image , (96 , 96))
        self.image = pygame.transform.rotate(self.image , degree)
        self.rect = self.image.get_rect(center = self.rect.center)



    def rotate_to_mouse(self):
        player_pos_x , player_pos_y = self.rect.center
        mouse_x , mouse_y = pygame.mouse.get_pos()
        x_interval = mouse_x - player_pos_x
        y_interval = mouse_y - player_pos_y
            
        # self.rotation = math.degrees(math.atan2(y_interval , x_interval))

        self.rotation = (180 / math.pi) * -math.atan2(y_interval , x_interval)

        self.rotation = int(self.rotation)
        self.image = self.original_image
        if not self.armed:
            self.image = pygame.transform.scale(self.image , (96 , 96))
        else:
            self.image = pygame.transform.scale(self.image , (96 , 96))
        self.image = pygame.transform.rotate(self.image , self.rotation)
        self.rect = self.image.get_rect(center = self.rect.center)


    def arm(self):
        self.armed = True
        self.original_image = pygame.image.load("resources\\images\\gunned_player_cookie.png")
        self.image = self.original_image
        self.image = pygame.transform.scale(self.image , (96,96))
        self.rect = self.image.get_rect(center = self.rect.center)





        
        
    def update(self):
        self.last_shot += 1
        self.get_input()
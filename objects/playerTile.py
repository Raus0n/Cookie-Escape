import pygame
import math

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
        self.speed = 2


    def get_input(self):
        keys = pygame.key.get_pressed()
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


    def rotate_to_mouse(self):
        player_pos_x , player_pos_y = self.rect.center
        mouse_x , mouse_y = pygame.mouse.get_pos()

        # x_interval = player_pos_x - mouse_x
        # y_interval = player_pos_y - mouse_y

        x_interval = mouse_x - player_pos_x
        y_interval = mouse_y - player_pos_y
            
        # self.rotation = math.degrees(math.atan2(y_interval , x_interval))

        self.rotation = (180 / math.pi) * -math.atan2(y_interval , x_interval)

        self.rotation = int(self.rotation)
        self.image = self.original_image
        self.image = pygame.transform.scale(self.image , (96 , 96))
        self.image = pygame.transform.rotate(self.image , self.rotation)
        self.rect = self.image.get_rect(center = self.rect.center)




        
        
    def update(self):
        self.rotate_to_mouse()
        self.get_input()
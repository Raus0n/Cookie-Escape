import pygame
from objects.playerTile import PlayerTile
from objects.tmnf import TMNFCar
import levels.level1 as level1
from shapes.borderTile import BorderTile
from shapes.tiles import Tile
class Level:

    def __init__(self, level_data , surface):
        self.level_data = level_data
        self.surface = surface
        self.world_shift_x = 0
        self.world_shift_y = 0
        self.world_border = 64
        self.setup_level(level_data , 1)

    def world_shifter(self):
        player = self.player.sprite
        playerX = player.rect.centerx
        playerY = player.rect.centery
        directionX = player.direction.x
        directionY = player.direction.y
        if playerX < self.world_border and directionX < 0:
            self.world_shift_x = 2
            player.speed = 0
        elif playerX > 960 - self.world_border and directionX > 0:
            self.world_shift_x = -2
            player.speed = 0
        elif playerY < self.world_border and directionY < 0:
            self.world_shift_y = 2
            player.speed = 0
        elif playerY > 960 - self.world_border and directionY > 0:
            self.world_shift_y = -2
            player.speed = 0
        else:
            self.world_shift_x = 0
            self.world_shift_y = 0
            player.speed = 2


    def setup_level(self, level_layout , level_number):
        self.tiles = pygame.sprite.Group()
        self.level_trigger = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.tmnf_group = pygame.sprite.GroupSingle()

        if level_number == 1:
            level_x_offset = level1.level_offset_x
            level_y_offset = level1.level_offset_y

        for row_index, row in enumerate(level_layout):
            for col_index, cell in enumerate(row):
                x = (col_index - level_x_offset) * 64
                y = (row_index - level_y_offset) * 64
                if cell == "X":
                    tile = Tile(64 ,(x,y) , "black")
                    self.tiles.add(tile)

                if cell == "P":
                    player = PlayerTile(64 , (x ,y) , "grey")
                    self.player.add(player)

                if cell == "b":
                    level_trigger = BorderTile((x,y) , (2,2))
                    self.level_trigger.add(level_trigger)

                
                    

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for tile in self.tiles.sprites():
            if tile.rect.colliderect(player.rect):
                if player.direction.x > 0:
                    player.rect.right = tile.rect.left
                    player.virtual_can_change = False
                if player.direction.x < 0:
                    player.rect.left = tile.rect.right
                    player.virtual_can_change = False



    def vertical_movement_collision(self):
        player = self.player.sprite
        player.rect.y += player.direction.y * player.speed

        for tile in self.tiles.sprites():
            if tile.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = tile.rect.top
                if player.direction.y < 0:
                    player.rect.top = tile.rect.bottom

    def level_change_collision(self):
        player = self.player.sprite
        for borderTile in self.level_trigger.sprites():
            if borderTile.rect.colliderect(player.rect):
                print("level change")


    def run(self):
        self.level_change_collision()
        self.level_trigger.draw(self.surface)
        self.level_trigger.update(self.world_shift_x , self.world_shift_y)
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.tmnf_group.draw(self.surface)
        self.tmnf_group.update()
        self.player.draw(self.surface)
        self.world_shifter()
        self.tiles.draw(self.surface)
        self.tiles.update(self.world_shift_x , self.world_shift_y)


    
import pygame
from objects.playerTile import PlayerTile
from objects.tmnf import TMNFCar

from shapes.tiles import Tile
class Level:

    def __init__(self, level_data , surface):
        self.level_data = level_data
        self.surface = surface
        self.setup_level(level_data)

    def setup_level(self, level_layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.tmnf_group = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(level_layout):
            for col_index, cell in enumerate(row):
                x = col_index * 64
                y = row_index * 64
                if cell == "X":
                    tile = Tile(64 ,(x,y) , "black")
                    self.tiles.add(tile)

                if cell == "P":
                    player = PlayerTile(64 , (x ,y) , "grey")
                    self.player.add(player)

                if cell == "T":
                    tmnfcar = TMNFCar((x , y))
                    self.tmnf_group.add(tmnfcar)
                    

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for tile in self.tiles.sprites():
            if tile.rect.colliderect(player.rect):
                if player.direction.x > 0:
                    player.rect.right = tile.rect.left
                if player.direction.x < 0:
                    player.rect.left = tile.rect.right

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.rect.y += player.direction.y * player.speed

        for tile in self.tiles.sprites():
            if tile.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = tile.rect.top
                if player.direction.y < 0:
                    player.rect.top = tile.rect.bottom


    def run(self):
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.tmnf_group.draw(self.surface)
        self.tmnf_group.update()
        self.player.draw(self.surface)
        self.tiles.draw(self.surface)


    
from pydoc import plain, plainpager
import pygame
from objects.ammo import Ammo
from objects.crown import Crown
from objects.crushableTile import CrushAbleTile
from objects.end import End
from objects.gunItem import GunItem
from objects.info import Info
from objects.monster import Monster
from objects.platform import Platform
from objects.playerTile import PlayerTile
from objects.rocket import Rocket
from objects.tmnf import TMNFCar
from objects.label import AmmoLabel, Label
import levels.level1 as level1
import levels.level2 as level2
import levels.level3 as level3
import levels.level4 as level4
import levels.level5 as level5
from objects.borderTile import BorderTile
from shapes.invisibleTile import InvisibleTile
from objects.killerTile import KillerTile
from shapes.tiles import Tile
from virtualPos import VirtualPos
class Level:

    def __init__(self, level_data , surface):
        self.player_dead = False
        self.level_x_offset = 0
        self.level_y_offset = 0
        self.level_data = level_data
        self.surface = surface
        self.world_shift_x = 0
        self.world_shift_y = 0
        self.world_border = 64
        self.level_number = 1
        self.setup_level(level_data , 1 ,"P")
        self.universal_speed = 2
        self.monster_dead = False
        self.hitSound = pygame.mixer.Sound(".\\resources\\sound\\hitsound.mp3")
        self.pickupSound = pygame.mixer.Sound(".\\resources\\sound\\ammoPickup.mp3")
        self.movable = True
        self.state = "Info"
        

    def world_shifter(self):
        player = self.player.sprite
        playerX = player.rect.centerx
        playerY = player.rect.centery
        directionX = player.direction.x
        directionY = player.direction.y
        if playerX < self.world_border and directionX < 0:
            self.world_shift_x = self.universal_speed
            player.speed = 0
        elif playerX > 960 - self.world_border and directionX > 0:
            self.world_shift_x = -self.universal_speed
            player.speed = 0
        elif playerY < self.world_border and directionY < 0:
            self.world_shift_y = self.universal_speed
            player.speed = 0
        elif playerY > 960 - self.world_border and directionY > 0:
            self.world_shift_y = -self.universal_speed
            player.speed = 0
        else:
            self.world_shift_x = 0
            self.world_shift_y = 0
            player.speed = self.universal_speed

    def laybrinth_shifter(self):
        player = self.player.sprite
        directionX = player.direction.x
        directionY = player.direction.y
        if directionX < 0:
            self.world_shift_x = self.universal_speed
            player.speed = 0
        elif directionX > 0:
            self.world_shift_x = -self.universal_speed
            player.speed = 0
        elif directionY < 0:
            self.world_shift_y = self.universal_speed
            player.speed = 0
        elif directionY > 0:
            self.world_shift_y = -self.universal_speed
            player.speed = 0
        else:
            self.world_shift_x = 0
            self.world_shift_y = 0
            player.speed = self.universal_speed

    def setup_level(self, level_layout , level_number , player_name):
        self.font = pygame.font.Font(".\\resources\\fonts\\VCR_OSD_MONO_1.001.ttf" , 64)
        self.dead_label = Label(self.surface , self.font , VirtualPos(0 , 0))


        self.tiles = pygame.sprite.Group()
        self.platform = pygame.sprite.Group()
        self.level_trigger = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.monster = pygame.sprite.GroupSingle()
        self.gun_item = pygame.sprite.GroupSingle()
        self.ammo_group = pygame.sprite.Group()
        self.level_number = level_number
        self.killer_group = pygame.sprite.Group()
        self.rocket = pygame.sprite.GroupSingle()
        self.crushable_tiles = pygame.sprite.Group()
        self.crown = pygame.sprite.GroupSingle()
        


        if level_number == 1:
            self.level_x_offset = level1.level_offset_x
            self.level_y_offset = level1.level_offset_y
        elif level_number == 2:
            self.level_x_offset = level2.level_offset_x
            self.level_y_offset = level2.level_offset_y
        elif level_number == 4:
            self.level_x_offset = level4.level_offset_x
            self.level_y_offset = level4.level_offset_y
        elif level_number == 5:
            self.level_x_offset = level5.level_offset_x 
            self.level_y_offset = level5.level_offset_y
            

        for row_index, row in enumerate(level_layout):
            for col_index, cell in enumerate(row):
                x = (col_index - self.level_x_offset) * 64
                y = (row_index - self.level_y_offset) * 64
                if cell == "X":
                    tile = Tile(64 ,(x,y) , "black")
                    self.tiles.add(tile)

                if cell == "M":
                    platform = Platform((x,y))
                    self.platform.add(platform)

                if cell == "A":
                    ammo = Ammo((x,y))
                    self.ammo_group.add(ammo)

                if cell == player_name:
                    player = PlayerTile(64 , (x ,y) , "grey")
                    self.player.add(player)

                if cell == "b":
                    invisibleTile = InvisibleTile((x,y))
                    self.tiles.add(invisibleTile)

                if cell == "K":
                    killerTile = KillerTile((x,y))
                    self.killer_group.add(killerTile)

                if cell == "G":
                    gunItem = GunItem((x,y))
                    self.gun_item.add(gunItem)
                
                if cell == "C":
                    monster = Monster((x,y))
                    self.monster.add(monster)

                if cell == "V":
                    crushableTile = CrushAbleTile(64 , (x,y))
                    self.crushable_tiles.add(crushableTile)

                if cell == "R":
                    rocket = Rocket((x,y))
                    self.rocket.add(rocket)

                if cell == "c":
                    crown = Crown((x,y))
                    self.crown.add(crown)

                try:
                    cell = int(cell)
                    level_trigger = BorderTile((x,y) , (2,2) , cell)
                    self.level_trigger.add(level_trigger)
                except:
                    pass

        self.ammo_label = AmmoLabel(self.surface , self.font  , VirtualPos(0 , 900))
        self.ammo_label.value = self.player.sprite.ammo

    def ammo_collider(self):
        player = self.player.sprite
        for ammo in self.ammo_group.sprites():
            if ammo.rect.colliderect(player.rect):
                player.ammo += 1
                self.ammo_group.remove(ammo)
                self.pickupSound.play()
                # self.ammo_label.value += 1

    def kill_collision_check(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for killer in self.killer_group.sprites():
            if killer.rect.colliderect(player.rect):
                self.player_dead = True
                self.world_shift_x = 0
                self.world_shift_y = 0
                
    def rocket_collider(self):
        try:
            if self.rocket.sprite.rect.colliderect(self.player.sprite.rect):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_e]:
                    self.state = "End"
        except:
            pass

    def pickup_gun(self):
        try:
            player = self.player.sprite
            if self.gun_item.sprite.rect.colliderect(player.rect):
                player.armed = True
                player.arm()
                self.pickupSound.play()
        except:
            pass

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for tile in self.tiles.sprites():
            if tile.rect.colliderect(player.rect):
                if player.direction.x > 0:
                    player.rect.right = tile.rect.left
                if player.direction.x < 0:
                    player.rect.left = tile.rect.right
                self.movable = False

        # for crushables in self.crushable_tiles.sprites():
        #     if crushables.rect.colliderect(player.rect):
        #         print("Before X:" , self.player.sprite.rect.x)
        #         if player.direction.x > 0:
        #             player.rect.right = tile.rect.left
        #         if player.direction.x < 0:
        #             player.rect.left = tile.rect.right
        #         print("After X:"  , self.player.sprite.rect.x)




    def vertical_movement_collision(self):
        player = self.player.sprite
        player.rect.y += player.direction.y * player.speed

        for tile in self.tiles.sprites():
            if tile.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = tile.rect.top
                if player.direction.y < 0:
                    player.rect.top = tile.rect.bottom

        # for crushables in self.crushable_tiles.sprites():
        #     if crushables.rect.colliderect(player.rect):
        #         print("Before Y:" , self.player.sprite.rect.y)
        #         if player.direction.y > 0:
        #             player.rect.bottom = tile.rect.top
        #         if player.direction.y < 0:
        #             player.rect.top = tile.rect.bottom
        #         print("After Y:" , self.player.sprite.rect.y)


    def lazer_collider(self , lazers: pygame.sprite.Group):
        for lazer in lazers.sprites():
            for tiles in self.tiles.sprites():
                if tiles.rect.colliderect(lazer.rect):
                    lazers.remove(lazer)
                    tiles.remove(self.tiles)
                    self.hitSound.play()

            for crushables in self.crushable_tiles.sprites():
                for lazer in lazers.sprites():
                    if crushables.rect.colliderect(lazer.rect):
                        lazers.remove(lazer)
                        self.crushable_tiles.remove(crushables)
                        self.hitSound.play()


    def level_change_collision(self):
        player = self.player.sprite
        for borderTile in self.level_trigger.sprites():
            if borderTile.rect.colliderect(player.rect):
                ammo_lab = self.ammo_label.value
                arm = player.armed
                rotation = player.rotation
                rocket = player.has_rocket
                ammo = player.ammo
                if borderTile.level_trigger_number == 1:
                    if self.level_number == 2:
                        temp = self.player.sprite.rect.x
                        level_layout = level1.level_map
                        self.level_number = 1
                        self.setup_level(level_layout , self.level_number , "P")
                        self.player.sprite.rect.x = temp
                    elif self.level_number == 3 or self.level_number == 4:
                        temp = self.player.sprite.rect.y
                        level_layout = level1.level_map
                        self.level_number = 1
                        self.setup_level(level_layout , self.level_number , "P")
                        self.player.sprite.rect.y = temp
                elif borderTile.level_trigger_number == 2:
                    temp = self.player.sprite.rect.x
                    level_layout = level2.level_map
                    self.level_number = 2
                    self.setup_level(level_layout , self.level_number , "P")
                    self.player.sprite.rect.x = temp
                elif borderTile.level_trigger_number == 3:
                    if self.level_number == 1:
                        level_layout = level3.level_map
                        self.level_number = 3
                        self.level_x_offset = 32
                        self.level_y_offset = 4
                        self.setup_level(level_layout ,self.level_number , "P")
                    elif self.level_number == 5:
                        level_layout = level3.level_map
                        self.level_number = 3
                        self.level_x_offset = -4
                        self.level_y_offset = 56
                        self.setup_level(level_layout ,self.level_number , "p")
                elif borderTile.level_trigger_number == 4:
                    temp = self.player.sprite.rect.y
                    level_layout = level4.level_map
                    self.level_number = 4
                    self.setup_level(level_layout , self.level_number , "P")
                    self.player.sprite.rect.y = temp
                elif borderTile.level_trigger_number == 5:
                    temp = self.player.sprite.rect.y
                    level_layout = level5.level_map
                    self.level_number = 5
                    self.setup_level(level_layout , self.level_number , "P")
                    self.player.sprite.rect.y = temp
                if arm:
                    self.player.sprite.arm()
                self.player.sprite.rotate(rotation)
                self.player.sprite.rotation = rotation
                self.player.sprite.has_rocket = rocket
                self.player.sprite.ammo = ammo
                # self.ammo_label.value = ammo_lab

            



    def run(self):

        # try:
        #     if not self.monster_dead:
        #         self.monster.draw(self.surface)
        #         self.monster.update(self.world_shift_x , self.world_shift_y , self.player.sprite)
        #         spit_group = self.monster.sprite.get_spit()
        #         spit_group.draw(self.surface)
        #         spit_group.update(self.world_shift_x , self.world_shift_y)
        # except:
        #     pass


        lazers = self.player.sprite.get_lasers_shot()
        lazers.draw(self.surface)
        lazers.update()

        #Collisions
        self.rocket_collider()
        self.ammo_collider()
        self.level_change_collision()
        self.lazer_collider(lazers)
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.kill_collision_check()

        if self.player.sprite.armed == False:
            self.gun_item.draw(self.surface)
            self.gun_item.update(self.world_shift_x , self.world_shift_y)
            self.pickup_gun()

        #Updates
        if self.state == "Game":
            if not self.player_dead:
                if  self.level_number == 3 or self.level_number == 5:
                    if self.movable:
                        self.laybrinth_shifter()
                else:
                    self.world_shifter()
            self.crown.update(self.world_shift_x , self.world_shift_y)
            self.ammo_group.update(self.world_shift_x , self.world_shift_y)
            self.crushable_tiles.update(self.world_shift_x , self.world_shift_y)
            self.rocket.update(self.world_shift_x , self.world_shift_y)
            self.platform.update(self.world_shift_x , self.world_shift_y)
            self.killer_group.update(self.world_shift_x , self.world_shift_y)
            self.level_trigger.update(self.world_shift_x , self.world_shift_y)
            self.tiles.update(self.world_shift_x , self.world_shift_y)
            if not self.player_dead:
                self.player.update()
            elif self.player_dead == True:
                self.world_shift_x = 0
                self.world_shift_y = 0

        #Drawings
        self.crown.draw(self.surface)
        self.ammo_group.draw(self.surface)
        self.crushable_tiles.draw(self.surface)
        self.rocket.draw(self.surface)
        self.platform.draw(self.surface)
        self.killer_group.draw(self.surface)
        self.level_trigger.draw(self.surface)
        if not self.player_dead:
            self.player.draw(self.surface)
        self.tiles.draw(self.surface)
        if self.player_dead:
            self.dead_label.render()
        self.ammo_label.value = self.player.sprite.ammo
        self.ammo_label.render()
        if self.state == "Info":
            font = pygame.font.Font(".\\resources\\fonts\\VCR_OSD_MONO_1.001.ttf" , 24)
            infoLabel = Info(font , self.surface)
            info_gr = pygame.sprite.GroupSingle()
            info_gr.add(infoLabel)
            info_gr.draw(self.surface)
            infoLabel.render()

        if self.state == "End":
            endLabel = End(self.surface) 
            endLabel.render()


    
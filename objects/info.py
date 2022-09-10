from cgitb import text
import pygame

class Info(pygame.sprite.Sprite):
    def __init__(self, font:pygame.font.Font , display):
        super().__init__()
        self.image = pygame.Surface((726 , 576))
        self.image.fill("white")
        self.rect = self.image.get_rect(topleft = (96 , 192))
        self.value = [" - You're an officer of Cookie Spaceguards" , " - You crashed into this red planet", " - There's a emergency rocket in this planet"  ," - Find the rocket and escape.", " - If you touch orange tiles, you die.", " - Use a gun to smash rocks." , " - Use WASD to move", " - Arrow Keys to rotate", " - R to reset", " - E to interact." , " - Tab to open or close this menu"]
        self.font = font
        self.display = display

    def render(self):
        for sen in range(len(self.value)):
            text = self.font.render(self.value[sen] , True , "black")
            self.display.blit(text , (self.rect.x , self.rect.y + (32 * sen)))

        self.display.blit(self.font.render("Paused" ,True , "black") , (0,0))

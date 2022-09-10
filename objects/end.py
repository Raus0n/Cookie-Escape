from re import S
import pygame

from virtualPos import VirtualPos

class End():
    def __init__(self,display) -> None:
        super().__init__()
        self.font = pygame.font.Font(".\\resources\\fonts\\VCR_OSD_MONO_1.001.ttf" , 128)
        self.font2 = pygame.font.Font(".\\resources\\fonts\\VCR_OSD_MONO_1.001.ttf" , 48)
        self.font3 = pygame.font.Font(".\\resources\\fonts\\VCR_OSD_MONO_1.001.ttf" , 32)
        self.display = display

    def render(self):
        self.display.fill("black")
        text = self.font.render("The end" , True , "white")
        text_rect = text.get_rect(center = (480 ,288))
        self.display.blit(text , text_rect)

        
        text2 = self.font2.render("Thanks for playing" , True , "white")
        text_rect = text2.get_rect(center = (480 ,416))
        self.display.blit(text2 , text_rect)
        
        text3 = self.font3.render("Code by testroyer" , True , "white")
        text_rect = text3.get_rect(center = (480 ,464))
        self.display.blit(text3 , text_rect)

        text4 = self.font3.render("Graphics by Phonem" , True , "white")
        text_rect = text4.get_rect(center = (480 ,496))
        self.display.blit(text4 , text_rect)
        
        text5 = self.font3.render("Honorable mention: Raus0n & Paramesyum" , True , "white")
        text_rect = text5.get_rect(center = (480 ,528))
        self.display.blit(text5 , text_rect)



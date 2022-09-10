import pygame 
from virtualPos import VirtualPos

class Label():
    def __init__(self , display,  font , pos:VirtualPos):
        super().__init__()
        self.value = "Game Over"
        self.pos = pos
        self.font = font
        self.display = display

    def render(self):
        text = self.font.render(self.value , True ,"black" )
        self.display.blit(text , (self.pos.x , self.pos.y))
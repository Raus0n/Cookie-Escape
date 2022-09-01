import pygame
from level import Level
import settings,os

pygame.init()

SCREEN_HEIGHT = 960
SCREEN_WIDTH = 960

BLACK = (0,0,0)
WHITE = (255,255,255)

FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
pygame.display.set_caption("Based Game")

level = Level(settings.level_map , screen)


def draw_screen():
    screen.fill((255,255,255))
    #şuraya çizilecek şeyleri koycaz işte, buraya level,resim vs koyacaksanız ayarlarsınız. bu arada resim loadlamak da çok kolaymış mesela örnek:
    pygame.display.update()
def main():
    
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        draw_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()


    level.run()
    

if __name__ == "__main__":
    main()
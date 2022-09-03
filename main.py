import pygame
from level import Level
import settings,os

pygame.init()

SCREEN_HEIGHT = 960
SCREEN_WIDTH = 960

TRACKMANIA_CAR = pygame.image.load("./resources/images/tm car.png")
TRACKMANIA_CAR_IMAGE = pygame.transform.scale(TRACKMANIA_CAR, (105,80))
TRACKMANIA_CAR_IMAGE = pygame.transform.rotate(TRACKMANIA_CAR_IMAGE, 40)

BLACK = (0,0,0)
WHITE = (255,255,255)

FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
pygame.display.set_caption("Based Game")

level = Level(settings.level_map , screen)


def draw_screen(tmnf):
    screen.blit(TRACKMANIA_CAR_IMAGE, (tmnf.x,tmnf.y))
    #şuraya çizilecek şeyleri koycaz işte, buraya level,resim vs koyacaksanız ayarlarsınız. bu arada resim loadlamak da çok kolaymış mesela örnek:
    pygame.display.update()



def main():
    # tmnf = pygame.Rect(100, 300, 105,80)
    clock = pygame.time.Clock()
    clock.tick(FPS)
    running = True
    while running:
        # draw_screen(tmnf)
        screen.fill("white")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        level.run()
        pygame.display.update()    

if __name__ == "__main__":
    main()
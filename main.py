import pygame
from level import Level
import levels.level1 as level1,os

pygame.init()

SCREEN_HEIGHT = 960
SCREEN_WIDTH = 960

BLACK = (0,0,0)
WHITE = (255,255,255)
RED_PLANET_BACKGROUND = (182, 54, 36)

FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
pygame.display.set_caption("Based Game")

level = Level(level1.level_map , screen)




def main():
    # tmnf = pygame.Rect(100, 300, 105,80)
    clock = pygame.time.Clock()
    clock.tick(FPS)
    running = True
    while running:
        # draw_screen(tmnf)
        screen.fill(RED_PLANET_BACKGROUND)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        level.run()
        pygame.display.update()    

if __name__ == "__main__":
    main()
import pygame
from level import Level
import levels.level1 as level1,os





def main():
    pygame.init()

    SCREEN_HEIGHT = 960
    SCREEN_WIDTH = 960

    BLACK = (0,0,0)
    WHITE = (255,255,255)
    RED_PLANET_BACKGROUND = (182, 54, 36)

    FPS = 60

    paper_sound = pygame.mixer.Sound(".\\resources\\sound\\info_open.mp3")

    screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
    pygame.display.set_caption("Cookie Escape")

    level = Level(level1.level_map , screen)
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
                    pygame.quit()
                if event.key == pygame.K_TAB:
                    if level.state == "Game":
                        level.state = "Info"
                        paper_sound.play()
                    elif level.state == "Info":
                        level.state = "Game"
                        paper_sound.play()


            

        level.run()
        pygame.display.update()    

if __name__ == "__main__":
    main()

import pygame
from clock import Clock
from constants import WIDTH, HEIGHT

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Analog Clock v1.0 by AW')
FPS = 60 # minimum 1

def main():
    run = True
    clock = pygame.time.Clock()
    clock_face = Clock(WIN)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                LMB, MMB, RMB = pygame.mouse.get_pressed(3)
                if LMB:
                    print(clock_face.get_hours())
                elif MMB:
                    print(clock_face.get_mins())
                elif RMB:
                    print(clock_face.get_secs())

        clock_face.update()

    pygame.quit()

main()

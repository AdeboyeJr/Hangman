import pygame
import word
from display import View

pygame.init()

WIDTH, HEIGHT = 600, 600

WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # instatiate pygame surface

pygame.display.set_caption("Hangman")


FONT = pygame.font.SysFont("comicsans", 16)

bg = pygame.image.load("images/hm_0.png").convert()


def main():

    run = True

    display = View(WIN, WIDTH, HEIGHT, bg)

    while run:
        # WIN.fill((0,0,0))

        # WIN.blit(bg, ((WIDTH/2) - 100, (HEIGHT/2) - 100))
        display.render()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()

    pass

if __name__ == '__main__':
    main()
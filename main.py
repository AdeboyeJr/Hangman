import pygame

pygame.init()

WIDTH, HEIGHT = 800, 800

WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # instatiate pygame surface

pygame.display.set_caption("Hangman")


FONT = pygame.font.SysFont("comicsans", 16)


def main():

    run = True

    while run:
        WIN.fill((0,0,0))

        # WIN.blit(bg, (0, 0))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                
        pygame.display.update()

    pygame.quit()

    pass

if __name__ == '__main__':
    main()
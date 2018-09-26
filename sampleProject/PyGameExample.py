import pygame
from pygame.locals import *

pygame.init()


def run():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Pygame Hello World")

    font = pygame.font.SysFont("Arial", 72)

    text = font.render("Hello World", True, (0, 128, 0))
    text_x = (screen.get_width() / 2) - (text.get_width() / 2)
    text_y = (screen.get_height() / 2) - (text.get_height() / 2)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN:
                return
            if event.type == MOUSEBUTTONDOWN:
                return

        screen.fill((255, 255, 255))
        screen.blit(text, (text_x, text_y))

        pygame.display.update()


if __name__ == '__main__':
    run()

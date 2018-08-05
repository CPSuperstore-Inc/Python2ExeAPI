import pygame
from pygame.locals import *
import text_format

pygame.init()

BOX_SHRINK = 30


def alert(screen, message, key_listener=[32]):
    message_font = pygame.font.SysFont("Courier New", 20)

    screen_w, screen_h = screen.get_size()
    box_w = int(round(screen_w * (BOX_SHRINK / 100.0), 0))
    box_h = int(round(screen_h * (BOX_SHRINK / 100.0), 0))

    message_text = text_format.wrapline(message, message_font, box_w)

    box_x = (screen_w / 2) - (box_w / 2)
    box_y = (screen_h / 2) - (box_h / 2)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
            if event.type == KEYDOWN:
                if event.key in key_listener:
                    return event.key

        pygame.draw.rect(screen, (200, 200, 200), (box_x, box_y, box_w, box_h), 0)

        index = 0
        for line in message_text:
            phrase = message_font.render(line, True, (0, 0, 0))

            screen.blit(phrase, ((screen_w / 2) - (phrase.get_size()[0] / 2), box_y + phrase.get_size()[1] * index))
            index += 1

        pygame.display.update()

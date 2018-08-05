import pygame
from pygame.locals import *

import time
import globalVariable

pygame.init()


class Timer:
    def __init__(self, screen, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.screen = screen

        self.timing = False
        self.start_time = 0

        self.font = pygame.font.SysFont("Courier New", 16)

        self.time = 0

    def start(self):
        self.timing = True
        self.start_time = time.time()

    def stop(self):
        self.timing = False

    def reset(self):
        self.timing = False
        self.start_time = 0
        self.time = 0

    def update(self):
        if self.timing is True:
            self.time = time.time() - self.start_time
        time_display = self.font.render("Time: {}".format(self.time), True, (255, 255, 255))
        level_display = self.font.render("Level: {}".format(globalVariable.SPEED), True, (255, 255, 255))
        self.screen.blit(time_display, (self.x_pos, self.y_pos))
        self.screen.blit(level_display, (self.x_pos, self.y_pos + time_display.get_size()[1]))
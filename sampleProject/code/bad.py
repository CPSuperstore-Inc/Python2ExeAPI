import pygame
import random
from pygame.locals import *

import globalVariable

pygame.init()


class BadHandler:
    def __init__(self, screen, image_list, line_array):
        self.screen = screen
        self.image_list = image_list
        self.line_array = line_array
        self.bad_dudes = []

        self.bad_size = int(round(globalVariable.LANE_WIDTH * (globalVariable.PLAYER_LANE_PERCENT / 100.0), 0 ))
        globalVariable.DELAY_DISTANCE = self.bad_size

    def update(self):
        y_pos = []
        for dude in self.bad_dudes:
            y_pos.append(dude.update())

        while True in y_pos: y_pos.remove(True)

        try:
            if min(y_pos) < globalVariable.DELAY_DISTANCE:
                spawn = False
            else:
                spawn = True
        except ValueError:
            spawn = True

        if spawn is True:
            self.bad_dudes.append(Bad(self.screen, random.choice(self.image_list), random.choice(self.line_array), self.bad_size))

    def is_touching(self, x_pos, y_pos, width, height):
        for dude in self.bad_dudes:
            if dude.is_touching(x_pos, y_pos, width, height) is True:
                return True

    def clear_bad_dudes(self):
        self.bad_dudes = []


class Bad:
    def __init__(self, screen, image, start_x, size):
        self.screen = screen
        self.screen_w, self.screen_h = screen.get_size()
        self.image = image
        self.object = pygame.transform.scale(pygame.image.load(image), (size, size))
        self.size = size
        self.start_x = start_x + ((globalVariable.LANE_WIDTH / 2) - (size / 2))
        self.y_pos = size / -1

    def update(self):
        self.screen.blit(self.object, (self.start_x, self.y_pos))
        self.y_pos += globalVariable.SPEED
        if self.y_pos > self.screen_h:
            del self
            return True

        return self.y_pos

    def is_touching(self, x_pos, y_pos, width, height):

        hit_box = pygame.draw.rect(self.screen, (200, 0, 0), (self.start_x, self.y_pos, self.size, self.size), 0)

        x_pos = int(round(x_pos, 0))
        y_pos = int(round(y_pos, 0))
        width = int(round(width, 0))
        height = int(round(height, 0))

        # get array of 4 corner of image
        corners = [(x_pos, y_pos),
                   (x_pos, y_pos + height),
                   (x_pos + width, y_pos),
                   (x_pos + width, y_pos + height)]

        for point in corners:
            if hit_box.collidepoint(point):
                return True


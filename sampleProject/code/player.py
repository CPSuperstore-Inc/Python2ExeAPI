import pygame
from pygame.locals import *

import globalVariable

pygame.init()

class Character:
    def __init__(self, screen, slot, image, lane_postitions):
        self.screen = screen
        self.screen_w, self.screen_h = screen.get_size()
        self.slot = slot
        self.image = image
        self.object = pygame.image.load(image)
        self.lane_postitions = lane_postitions

        # get the original size
        original_w, original_h = self.object.get_size()

        # calculate the new image width
        # the width of hte play are will be half of the screen.
        # there will be four lanes
        # the player will be three thirds of hte lane size. MATH IS NEEDED!
        
        new_w = self.screen_w * globalVariable.BOARD_PERCENT / 100.0
        new_w /= float(globalVariable.LANES)
        new_w *= globalVariable.PLAYER_LANE_PERCENT / 100.0

        # from this value, the proportional height is needed.
        # find the multiplication factor
        multiplier = new_w / original_w
        new_h = original_h * multiplier

        # apply the transformation
        self.object = pygame.transform.scale(self.object, (int(round(new_w, 0)), int(round(new_h, 0))))
        self.width, self.height = self.object.get_size()

        self.x_pos = self.x_pos = lane_postitions[self.slot] + ((globalVariable.LANE_WIDTH / 2) - (new_w / 2))
        self.y_pos = self.screen_h - int(round(new_h, 0))


    def update(self):
        self.screen.blit(self.object, (self.x_pos, self.y_pos))

    def change_lane(self, amount):

        if globalVariable.PLAY is True:
        
            self.slot += amount
            if self.slot < 0:
                self.slot -= amount
            else:
                try:

                    self.x_pos = self.x_pos = self.lane_postitions[self.slot] + ((globalVariable.LANE_WIDTH / 2) - (self.width / 2))
                except IndexError:
                    self.slot -= amount

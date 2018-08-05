import pygame
from pygame.locals import *

import time

import globalVariable
import player as character
import bad as bad_dude
import timer as hud_timer
from notification import *

pygame.init()


def run(screen=None):

    # check if there is a screen object passed in
    if screen is None:
        # if there is no screen, create one
        # Make the screen windowed (1050x450)
        screen_w = 1050
        screen_h = 450
        mode = RESIZABLE            # 0 = windowed

        # Create Surface
        screen = pygame.display.set_mode((screen_w, screen_h), mode, 32)

    else:
        screen_w, screen_h = screen.get_size()

    # Set caption
    pygame.display.set_caption(globalVariable.NAME)

    # Create clock object
    clock = pygame.time.Clock()

    # create "player" object

    # calculate the width of the play area
    play_area_width = screen_w / 2

    # calculate the width of a lane
    globalVariable.LANE_WIDTH = play_area_width / globalVariable.LANES

    # Generate an array of line points for the lane dividers
    line_array = []
    for line in range(globalVariable.LANES + 1):
        line_array.append([((screen_w / 2) - (screen_w / 4) + (globalVariable.LANE_WIDTH * line), 0),
                           ((screen_w / 2) - (screen_w / 4) + (globalVariable.LANE_WIDTH * line), screen_h)])

    line_array_x_pos = []
    for line in range(globalVariable.LANES):
        line_array_x_pos.append((screen_w / 2) - (screen_w / 4) + (globalVariable.LANE_WIDTH * line))

    # create the original player object    
    player = character.Character(screen, 0, 'images/player/player_fwd.png', line_array_x_pos)

    timer = hud_timer.Timer(screen, 0, 0)

    # create enemy object
    image_list = ['images/bad/bad_fwd.png']
    bad = bad_dude.BadHandler(screen, image_list, line_array_x_pos)

    start_time = time.time()

    prompt = False

    timer.start()

    while True:
        if time.time() - start_time >= globalVariable.LEVEL_UP:
            if globalVariable.PLAY is True:
                globalVariable.SPEED += 1
                start_time = time.time()

        for event in pygame.event.get():
            if event.type == QUIT:
                quit()

            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    player.change_lane(-1)
                if event.key == K_RIGHT:
                    player.change_lane(1)
            if event.type == VIDEORESIZE:
                screen_w = event.dict['size'][0]
                screen_h = event.dict['size'][1]
                screen = pygame.display.set_mode((screen_w, screen_h), HWSURFACE | DOUBLEBUF | RESIZABLE)

        if bad.is_touching(player.x_pos, player.y_pos, player.width, player.height) is True:
            timer.stop()
            globalVariable.PLAY = False
            prompt = True

        # fill the screen
        screen.fill((0, 0, 0))

        # draw the rectangle play area
        pygame.draw.rect(screen, (200, 0, 0), ((int(round(screen_w * (globalVariable.BOARD_PERCENT / 100.0), 0))) - (screen_w / 4), 0, play_area_width, screen_h), 0)

        for line in line_array:
            pygame.draw.lines(screen, (0, 255, 0), False, line, 5)

        # draw the player, and bad dudes
        player.update()
        if globalVariable.PLAY is True:
            bad.update()
        timer.update()

        # update the screen
        pygame.display.update()

        # limit to 60 FPS
        clock.tick(globalVariable.MAX_FRAME_RATE)

        if prompt is True:
            response = alert(screen, "You Have Died! Press 'SPACE' To Play Again, Or 'ESCAPE' To Quit", key_listener=[32, 27])
            if response == 32:
                bad.clear_bad_dudes()
                # reset game
                globalVariable.PLAY = True
                globalVariable.SPEED = 1
                timer.reset()
                timer.start()
                start_time = time.time()
                prompt = False
            elif response == 27:
                quit()

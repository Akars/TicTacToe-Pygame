import pygame
import game
import sys
from game import *
from pygame.locals import *

pygame.init()


def interface():
    screen_size = Coordinate(600, 600)
    screen = pygame.display.set_mode((screen_size['x'], screen_size['y']))
    pygame.display.flip()
    for i in range(2):
        i = i + 1
        interspace_x = screen_size['x']/3
        interspace_y = screen_size['y']/3
        pygame.draw.line(screen, (255, 255, 255), (interspace_x * i, 0), (interspace_x * i, screen_size['y']), 1)
        pygame.draw.line(screen, (255, 255, 255), (0, interspace_y * i), (screen_size['x'], interspace_y * i), 1)


def main():
    interface()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()


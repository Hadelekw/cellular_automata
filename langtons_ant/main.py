"""
 Implementation of Langton's Ant.
 Usage: ./main.py <dimension> [scaling=1]
"""

import pygame as pg
import numpy as np
import random
import sys


class Ant:
    directions = {
        'left': [-1, 0],
        'right': [1, 0],
        'up': [0, -1],
        'down': [0, 1],
    }

    def __init__(self, pos):
        self.pos = pos
        self.direction = self.directions['up']

    def rotate_clockwise(self):
        if self.direction == self.directions['up']:
            self.direction = self.directions['right']
        elif self.direction == self.directions['right']:
            self.direction = self.directions['down']
        elif self.direction == self.directions['down']:
            self.direction = self.directions['left']
        else:
            self.direction = self.directions['up']

    def rotate_anticlockwise(self):
        if self.direction == self.directions['up']:
           self.direction = self.directions['left']
        elif self.direction == self.directions['left']:
            self.direction = self.directions['down']
        elif self.direction == self.directions['down']:
            self.direction = self.directions['right']
        else:
            self.direction = self.directions['up']


def main(dim, scale=1):
    grid = np.array([[0 for __ in range(dim)] for _ in range(dim)], np.int8)
    visited = []

    ant = Ant(pos=[dim // 2, dim // 2])

    screen = pg.display.set_mode([dim * scale, dim * scale])
    clock = pg.time.Clock()

    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False
        screen.fill((0, 0, 0))

        if not ant.pos in visited:
            ant.rotate_clockwise()
            visited.append([ant.pos[0], ant.pos[1]])
        else:
            ant.rotate_anticlockwise()
            visited.remove(ant.pos)
        ant.pos[0] += ant.direction[0]
        ant.pos[1] += ant.direction[1]

        for tile in visited:
            pg.draw.rect(screen,
                         (255, 255, 255),
                         pg.Rect(tile[0] * scale,
                                 tile[1] * scale,
                                 scale, scale)
                         )
        pg.display.flip()
    pg.quit()


if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]))

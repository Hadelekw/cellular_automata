"""
 Implementation of Maze algorithm.
 Usage: ./main.py <dimension> [scaling=1]
"""

import pygame as pg
import numpy as np
import random
import sys


def check_neighbors(grid, dim, kernel=np.array([[1, 1, 1],
                                                [1, 0, 1],
                                                [1, 1, 1],])):
    neighbors_count = {}
    check_i, check_j = 0, 0
    for j in range(2, dim - 2):
        check_j = j + 1
        for i in range(2, dim - 2):
            check_i = i + 1
            neighbors_count[(i, j)] = 0
            for kernel_j in range(0, 3):
                for kernel_i in range(0, 3):
                    if grid[i + kernel_i - 1, j + kernel_j - 1] * kernel[kernel_i, kernel_j]:
                        neighbors_count[(i, j)] += 1
    for pos, count in neighbors_count.items():
        if grid[pos]:
            if count < 5:
                grid[pos] = 1
            if count > 5:
                grid[pos] = 0
        else:
            if count == 3:
                grid[pos] = 1


def main(dim, scale=1):
    grid = np.array([[0 for __ in range(dim)] for _ in range(dim)], np.int8)

    for j in range(2, dim - 2):
        for i in range(2, dim - 2):
            grid[i, j] = random.randint(0, 1)

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

        for j in range(dim):
            for i in range(dim):
                if grid[i, j]:
                    pg.draw.rect(screen, (255, 255, 255), pg.Rect(i * scale, j * scale, scale, scale))
        check_neighbors(grid, dim)

        clock.tick(60)
        pg.display.flip()
    pg.quit()

if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]))

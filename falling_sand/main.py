"""
 Simple falling sand implementation.
 Usage: ./main.py <dimension> [scaling=1]
"""

import pygame as pg
import numpy as np
import copy
import sys


def main(dim, scale=1):
    grid = np.array([[0 for __ in range(dim)] for _ in range(dim)])
    grid[dim // 2, dim // 2] = 1
    set_sand = False

    screen = pg.display.set_mode([dim * scale, dim * scale])
    clock = pg.time.Clock()

    run = True
    while run:
        mx, my = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    set_sand = True
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    set_sand = False
        screen.fill((0, 0, 0))

        buf = copy.deepcopy(grid)
        for i in range(dim):
            for j in range(dim)[::-1]:
                if grid[i, j]:
                    pg.draw.rect(screen, (int(i / dim * 255), int(j / dim * 255), 255), pg.Rect(i * scale, j * scale, scale, scale))
                    if j + 1 != dim and i - 1 > -1 and i + 1 < dim:
                        if not buf[i, j + 1]:
                            buf[i, j] = 0
                            buf[i, j + 1] = 1
                        elif not buf[i - 1, j + 1]:
                            buf[i, j] = 0
                            buf[i - 1, j + 1] = 1
                        elif not buf[i + 1, j + 1]:
                            buf[i, j] = 0
                            buf[i + 1, j + 1] = 1
        grid = buf

        if set_sand:
            grid[mx // scale, my // scale] = 1

        clock.tick(60)
        pg.display.flip()
    pg.quit()


if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]))

"""
 Implementation of one dimensional cellular automata rules.
 Usage: ./main.py <rule_number> <dimension> [scaling=1]
"""

import pygame as pg
import numpy as np
import sys


def step(line, rule, kernel=np.array([1, 1, 1])):
    states = [(1, 1, 1), (1, 1, 0), (1, 0, 1), (1, 0, 0), (0, 1, 1), (0, 1, 0), (0, 0, 1), (0, 0, 0)]
    ruleset = {states[i]: rule[i] for i in range(len(states))}
    result = [0 for _ in line]
    for i in range(1, len(line) - 1):
        neighborhood = []
        for j in range(-1, 2):
            neighborhood.append(line[i + j])
        result[i] = ruleset[tuple(neighborhood)]
    return result


def main(rule_number, dim, scale=1):
    grid = np.array([[0 for __ in range(dim)] for _ in range(dim)], np.int8)
    grid[0, dim // 2] = 1

    screen = pg.display.set_mode([dim * scale, dim * scale])
    clock = pg.time.Clock()

    rule = '{:b}'.format(rule_number)
    rule = rule.rjust(8, '0')

    current_line = 0

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
                if grid[j, i]:
                    pg.draw.rect(screen, (255, 255, 255), pg.Rect(i * scale, j * scale, scale, scale))
        grid[current_line + 1] = step(grid[current_line], rule)
        if current_line < len(grid) - 2:
            current_line += 1

        clock.tick(60)
        pg.display.flip()
    pg.quit()


if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

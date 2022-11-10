#!/usr/bin/env python3
# coding: utf-8

import random
from tkinter import *

WINDOW_WIDTH = 1700
WINDOW_HEIGHT = 900

CELL_SIZE = 10
DELAY = 50


def generate_random_grid():
    initial_grid = [[0] * (WINDOW_WIDTH // CELL_SIZE) for _ in range(WINDOW_HEIGHT // CELL_SIZE)]
    for y in range(len(initial_grid)):
        for x in range(len(initial_grid[0])):
            if random.randint(1, 200) == 1:
                initial_grid[y][x] = 1
    return initial_grid


def random_hex_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)


class Ball:

    def __init__(self, canvas, grid, position):
        self.canvas = canvas
        self.grid = grid
        self.x, self.y = position
        self.direction_x = 1
        self.direction_y = -1
        self.color = random_hex_color()
        self.rect = None
        self.update()

    def update(self):
        # print(self.y + self.direction_y, self.x + self.direction_x)
        if not (0 <= self.x + self.direction_x < len(self.grid[0])):
            self.direction_x = -self.direction_x
        if not (0 <= self.y + self.direction_y < len(self.grid)):
            self.direction_y = -self.direction_y
        if self.grid[self.y + self.direction_y][self.x + self.direction_x] == 1:
            self.direction_x = -self.direction_x
            self.direction_y = -self.direction_y
        if not (0 <= self.x + self.direction_x < len(self.grid[0])):
            self.direction_x = -self.direction_x
        if not (0 <= self.y + self.direction_y < len(self.grid)):
            self.direction_y = -self.direction_y
        if self.grid[self.y + self.direction_y][self.x + self.direction_x] != 1:
            self.grid[self.y][self.x] = 0
            self.x += self.direction_x
            self.y += self.direction_y
            self.grid[self.y][self.x] = 1
        self.draw()
        self.canvas.after(DELAY, self.update)

    def draw(self):
        if self.rect is not None:
            self.canvas.delete(self.rect)
        self.rect = self.canvas.create_rectangle(
            self.x * CELL_SIZE,
            self.y * CELL_SIZE,
            self.x * CELL_SIZE + CELL_SIZE,
            self.y * CELL_SIZE + CELL_SIZE,
            fill=self.color,
        )


master = Tk()
canvas = Canvas(master, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
canvas.pack()

initial_grid = generate_random_grid()

for y in range(len(initial_grid)):
    for x in range(len(initial_grid[0])):
        if initial_grid[y][x] == 1:
            Ball(canvas, initial_grid, (x, y))

master.mainloop()

import curses
import random

# 定义各种形状的方块
shapes = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 0], [0, 1, 1], [0, 0, 1]],
]

def draw_matrix(win, matrix, offset):
    for y, row in enumerate(matrix):
        for x, cell in enumerate(row):
            if cell:
                win.addch(y + offset[1], x + offset[0], "#")

def main(stdscr):
    curses.curs_set(0)
    win = curses.newwin(20, 20, 0, 0)

    current_shape = random.choice(shapes)
    shape_pos = [0, 0]

    while True:
        win.clear()
        draw_matrix(win, current_shape, shape_pos)
        win.refresh()

        key = win.getch()

        if key == curses.KEY_DOWN:
            shape_pos[1] += 1
        elif key == curses.KEY_UP:
            shape_pos[1] -= 1
        elif key == curses.KEY_RIGHT:
            shape_pos[0] += 1
        elif key == curses.KEY_LEFT:
            shape_pos[0] -= 1

if __name__ == "__main__":
    curses.wrapper(main)

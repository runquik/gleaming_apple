#!/usr/bin/env python3
"""Conway's Game of Life in the terminal."""

import argparse
import os
import random
import sys
import time


PATTERNS = {
    "glider": {
        "cells": [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
        "description": "The classic glider, drifting southeast.",
    },
    "pulsar": {
        "cells": [
            # Top-left quadrant (and mirrored)
            (2, 4), (2, 5), (2, 6), (2, 10), (2, 11), (2, 12),
            (4, 2), (4, 7), (4, 9), (4, 14),
            (5, 2), (5, 7), (5, 9), (5, 14),
            (6, 2), (6, 7), (6, 9), (6, 14),
            (7, 4), (7, 5), (7, 6), (7, 10), (7, 11), (7, 12),
            (9, 4), (9, 5), (9, 6), (9, 10), (9, 11), (9, 12),
            (10, 2), (10, 7), (10, 9), (10, 14),
            (11, 2), (11, 7), (11, 9), (11, 14),
            (12, 2), (12, 7), (12, 9), (12, 14),
            (14, 4), (14, 5), (14, 6), (14, 10), (14, 11), (14, 12),
        ],
        "description": "Period-3 oscillator. Mesmerizing.",
    },
    "gosper-gun": {
        "cells": [
            (5, 1), (5, 2), (6, 1), (6, 2),
            (5, 11), (6, 11), (7, 11),
            (4, 12), (8, 12),
            (3, 13), (9, 13),
            (3, 14), (9, 14),
            (6, 15),
            (4, 16), (8, 16),
            (5, 17), (6, 17), (7, 17),
            (6, 18),
            (3, 21), (4, 21), (5, 21),
            (3, 22), (4, 22), (5, 22),
            (2, 23), (6, 23),
            (1, 25), (2, 25), (6, 25), (7, 25),
            (3, 35), (4, 35), (3, 36), (4, 36),
        ],
        "description": "Gosper's glider gun. Infinite growth.",
    },
}

ALIVE = "\u2588\u2588"  # Full block, doubled for squareness
DEAD = "  "


def make_grid(width, height):
    return [[False] * width for _ in range(height)]


def random_fill(grid, density):
    height = len(grid)
    width = len(grid[0])
    for y in range(height):
        for x in range(width):
            grid[y][x] = random.random() < density


def place_pattern(grid, pattern_name):
    height = len(grid)
    width = len(grid[0])
    pattern = PATTERNS[pattern_name]
    cells = pattern["cells"]

    # Center the pattern
    max_y = max(y for y, x in cells)
    max_x = max(x for y, x in cells)
    offset_y = (height - max_y) // 2
    offset_x = (width - max_x) // 2

    for y, x in cells:
        ny, nx = y + offset_y, x + offset_x
        if 0 <= ny < height and 0 <= nx < width:
            grid[ny][nx] = True


def count_neighbors(grid, y, x):
    height = len(grid)
    width = len(grid[0])
    count = 0
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dy == 0 and dx == 0:
                continue
            ny = (y + dy) % height
            nx = (x + dx) % width
            if grid[ny][nx]:
                count += 1
    return count


def step(grid):
    height = len(grid)
    width = len(grid[0])
    new_grid = make_grid(width, height)
    for y in range(height):
        for x in range(width):
            n = count_neighbors(grid, y, x)
            if grid[y][x]:
                new_grid[y][x] = n in (2, 3)
            else:
                new_grid[y][x] = n == 3
    return new_grid


def render(grid, generation, population):
    lines = []
    for row in grid:
        lines.append("".join(ALIVE if cell else DEAD for cell in row))
    frame = "\n".join(lines)
    status = f" Gen: {generation}  |  Pop: {population}  |  Ctrl+C to quit"
    return f"\033[H\033[J{frame}\n{status}"


def count_alive(grid):
    return sum(cell for row in grid for cell in row)


def run(width, height, density, speed, pattern):
    grid = make_grid(width, height)

    if pattern:
        place_pattern(grid, pattern)
    else:
        random_fill(grid, density)

    generation = 0

    # Hide cursor
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

    try:
        while True:
            population = count_alive(grid)
            sys.stdout.write(render(grid, generation, population))
            sys.stdout.flush()
            time.sleep(speed)
            grid = step(grid)
            generation += 1
    except KeyboardInterrupt:
        pass
    finally:
        # Show cursor again
        sys.stdout.write("\033[?25h\n")
        sys.stdout.flush()
        print(f"Stopped after {generation} generations.")


def get_terminal_size():
    try:
        cols, rows = os.get_terminal_size()
        # Divide cols by 2 because each cell is 2 chars wide
        # Subtract a few rows for status line
        return cols // 2, rows - 2
    except OSError:
        return 40, 20


def main():
    default_w, default_h = get_terminal_size()

    parser = argparse.ArgumentParser(description="Conway's Game of Life in the terminal.")
    parser.add_argument("--width", type=int, default=default_w, help="Grid width in cells")
    parser.add_argument("--height", type=int, default=default_h, help="Grid height in cells")
    parser.add_argument("--density", type=float, default=0.3, help="Initial fill density (0.0-1.0)")
    parser.add_argument("--speed", type=float, default=0.15, help="Seconds between frames")
    parser.add_argument(
        "--pattern",
        choices=list(PATTERNS.keys()),
        default=None,
        help="Start with a named pattern instead of random",
    )
    args = parser.parse_args()

    if args.pattern:
        print(f"Pattern: {args.pattern} — {PATTERNS[args.pattern]['description']}")
        time.sleep(1)

    run(args.width, args.height, args.density, args.speed, args.pattern)


if __name__ == "__main__":
    main()

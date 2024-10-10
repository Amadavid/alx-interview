#!/usr/bin/python3
"""
    Module implementing island perimeter problem.

"""


def island_perimeter(grid):
    """Computes the perimeter of an island"""
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:   # land cell found
                # check the top side
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1

                # check the bottom side
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1

                # check the left side
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1

                # check the right side
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1

    return perimeter

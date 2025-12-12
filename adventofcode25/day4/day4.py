"""
Advent of code 2025 - Day 3 - Part 1 & 2
https://adventofcode.com/2025/day/3
"""

import os
import sys

# Add the root directory to the path so we can import aoc_utils
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, root_dir)

from aoc_utils.aoc_utils import Timer, get_data  # noqa: E402

data = get_data()
timer = Timer()

# ..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.

# a rolls is accessible only if there are less than 4 rolls in the 8 adjacent positions


def is_accessible(x, y):
    """
    return a position of a roll (@) if there are less than 4 rolls in the 8 adjacent positions
    """
    numbers_of_rolls_adjacent = 0
    for i in range(max(0, x - 1), min(len(data), x + 2)):
        for j in range(max(0, y - 1), min(len(data[0]), y + 2)):
            if data[i][j] == "@":
                numbers_of_rolls_adjacent += 1
    return numbers_of_rolls_adjacent - 1 < 4, numbers_of_rolls_adjacent - 1


numbers_of_accessible_rolls = 0
for i, row in enumerate(data):
    for j, col in enumerate(row):
        if col == "@" and is_accessible(i, j)[0]:
            numbers_of_accessible_rolls += 1

print(numbers_of_accessible_rolls)

# part 2, remove the accessible, and redo the process until no accessible rolls are left
# need to count all removed rolls


def remove_accessible_rolls(data):
    data_list = [list(row) for row in data]
    removed_rolls = 0
    for i, row in enumerate(data_list):
        for j, col in enumerate(row):
            if col == "@" and is_accessible(i, j)[0]:
                data_list[i][j] = "."
                removed_rolls += 1
    return ["".join(row) for row in data_list], removed_rolls


numbers_of_removed_rolls = 0
while True:
    new_data, removed_rolls = remove_accessible_rolls(data)
    if new_data == data:
        break
    data = new_data.copy()
    numbers_of_removed_rolls += removed_rolls

print(numbers_of_removed_rolls)

"""
Advent of code 2025 - Day 1 - Part 1 & 2
https://adventofcode.com/2025/day/1
"""

import os
import sys

# Add the root directory to the path so we can import aoc_utils
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, root_dir)

from aoc_utils.aoc_utils import Timer, get_data, print_solution  # noqa: E402

data = get_data()
timer = Timer()


directions = {"L": -1, "R": 1}

# Part 1

# 0 to 99
# so when P = 50 & move is L68 -> P = 82

position = 50

password = 0  # number of times the password is "0"

for move in data:
    direction = move[0]
    steps = int(move[1:])
    position = (position + steps * directions[direction]) % 100
    if position == 0:
        password += 1

print_solution(password, timer=timer)

# Part 2

# Count when the the dial shows "0", but also when we pass through it.
# Be careful: if the dial were pointing at 50, a single rotation like R1000 would cause
# the dial to point at 0 ten times before returning back to 50!

position = 50
password = 0

for move in data:
    direction = move[0]
    steps = int(move[1:])
    old_position = position

    if direction == "R":
        password += (position + steps) // 100

        position = (position + steps) % 100

    elif direction == "L":
        # Distance to reach 0 by moving left
        dist_vers_zero = position if position > 0 else 100

        if steps >= dist_vers_zero:
            # We have reached 0 at least once
            # We add 1 (first passage) + the remaining complete tours
            password += 1 + (steps - dist_vers_zero) // 100

        position = (position - steps) % 100


print_solution(p2=password, timer=timer)

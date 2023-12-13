"""
Advent of code 2023 - Day 12 - Part 1 & 2
https://adventofcode.com/2023/day/12
"""

import os
from functools import cache
import time

path = os.path.dirname(os.path.realpath(__file__))
FILE = path + "/data.txt"

with open(FILE, "r", encoding="utf-8") as f:
    data = []
    data = f.read().splitlines()

data = [
    [
        instruction.split()[0],
        tuple(int(arg) for arg in instruction.split(" ")[1].split(","))
    ]
    for instruction in data
]

@cache
def arrangements(lava, springs, result=0):
    """Recursively find all possible paths through the lava."""
    if not springs:
        return '#' not in lava

    current_spring, remaining_springs = springs[0], springs[1:]

    for i in range(
        len(lava) - sum(remaining_springs) - len(remaining_springs) - current_spring + 1
        ):
        if "#" in lava[:i]:
            break

        next_position = i + current_spring
        if (
            next_position <= len(lava)
            and '.' not in lava[i:next_position]
            and lava[next_position:next_position + 1] != "#"
        ):
            result += arrangements(lava[next_position + 1:], remaining_springs)

    return result



def solve(input_data):
    """Solve both parts of the problem."""
    t1 = time.time()
    p1, p2 = 0, 0
    for (i, j) in input_data:
        p1 += arrangements(i, j)
        p2 += arrangements("?".join([i]*5), j * 5)
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")
    print(f"Time: {time.time() - t1:.4f}s")

solve(data)

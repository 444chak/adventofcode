# pylint: disable=W0603
"""
Advent of code 2023 - Day 14 - Part 1 & 2
https://adventofcode.com/2023/day/14
"""

import os
import time
path = os.path.dirname(os.path.realpath(__file__))
FILE = path + "/data.txt"


with open(FILE, "r", encoding="utf-8") as f:
    data = f.read().splitlines()

def count_o(input_data):
    """Count the number of O in the data with strength"""
    return sum([i.count("O")*(len(i)-j) for j, i in enumerate(input_data)])

def east(nd):
    """Tilt the data to the east"""
    for i, line in enumerate(nd):
        while "O." in line:
            line = line.replace("O.", ".O")
            nd[i] = line
    return nd

def west(nd):
    """Tilt the data to the west"""
    for i, line in enumerate(nd):
        while ".O" in line:
            line = line.replace(".O", "O.")
            nd[i] = line
    return nd

def north(nd):
    """Tilt the data to the north"""
    return ["".join(i) for i in list(zip(*west(["".join(i) for i in zip(*nd)])))]


def south(nd):
    """Tilt the data to the south"""
    return ["".join(i) for i in list(zip(*east(["".join(i) for i in zip(*nd)])))]

def cycle(nd):
    """Cycle the data"""
    return east(south(west(north(nd))))


print("Part1 : ",count_o(north(data)))

t0 = time.time()
for _ in range(1000):
    data = cycle(data)
print("Part2 : ",count_o(data))
print(f"Time P2 : {time.time()-t0:.4f}s")

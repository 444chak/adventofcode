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

ids = [data[0].split(",")][0]

# convert into array of tuples
ids = [tuple(map(int, id.split("-"))) for id in ids]

print(ids)


# Part 1
invalid_ids = []
for i in range(0, 1000000):
    possible_invalid = int(str(i) * 2)
    for left, right in ids:
        if possible_invalid >= left and possible_invalid <= right:
            invalid_ids.append(possible_invalid)
            break

print_solution(p1=sum(invalid_ids), timer=timer)

# Part 2

invalid_ids = set()
for i in range(0, 100000):
    for times in range(2, 11):
        possible_invalid = int(str(i) * times)
        for left, right in ids:
            if possible_invalid >= left and possible_invalid <= right:
                invalid_ids.add(possible_invalid)
                break
print_solution(p2=sum(invalid_ids), timer=timer)

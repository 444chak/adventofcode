"""
Advent of code 2024 - Day 1 - Part 1 & 2
https://adventofcode.com/2024/day/1
"""

import os

# get path of the file
path = os.path.dirname(os.path.realpath(__file__))
FILE = path + "/data.txt"

left = []
right = []

with open(FILE, "r", encoding="utf-8") as f:
    for i in f.readlines():
        left.append(int(i.split()[0]))
        right.append(int(i.split()[1]))


# Part 1

dist = 0

new_left = left.copy()
new_right = right.copy()

for i in range(len(new_left)):
    min_left = min(new_left)
    min_right = min(new_right)
    new_left.remove(min_left)
    new_right.remove(min_right)
    dist += abs(min_left - min_right)


print(dist)

# Part 2

print(sum([i * right.count(i) for i in left]))

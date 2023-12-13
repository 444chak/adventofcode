"""
Advent of code 2023 - Day 10 - Part 1 & 2
https://adventofcode.com/2023/day/10
"""

import os
import time

path = os.path.dirname(os.path.realpath(__file__))
FILE = path + "/data.txt"


with open(FILE, "r", encoding="utf-8") as f:
    data = []
    data = f.read().splitlines()


loop = {}
for y, line in enumerate(data):
    for x, c in enumerate(line):
        if c != ".":
            loop[(x, y)] = c

start = list(loop.keys())[list(loop.values()).index('S')]


N, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0)

DIRS = {'S': [N, S, W, E],
        '|': [N, S], '-': [E, W],
        'L': [N, E], 'J': [N, W], 
        '7': [S, W], 'F': [S, E]}

NEXT = {N: {'|', '7', 'F'},
        S: {'|', 'L', 'J'},
        E: {'-', 'J', '7'},
        W: {'-', 'L', 'F'}}

# N, S, W, E, DIRS & NEXT by u/Gravitar64 (reddit)


# ------------------ PART 1 ------------------ #

t = time.time()

start = list(loop.keys())[list(loop.values()).index('S')]

waiting = [(0, start)]
view = set()
while waiting: # tant que la liste n'est pas vide
    part1, (x, y) = waiting.pop(0)
    view.add((x, y))
    for dir_x, dir_y in DIRS[loop[x, y]]: # on parcours les directions
        next_pos = x + dir_x, y + dir_y
        if (next_pos not in loop or next_pos in view) or (loop[next_pos] not in NEXT[dir_x, dir_y]):
            continue
        waiting.append((part1 + 1, next_pos))

print(f"Part 1: {part1} took {time.time() - t:.4f}s")


# ------------------ PART 2 ------------------ #

t = time.time()
viewed_loop = {}
for k,v in loop.items():
    if k in view:
        viewed_loop[k] = v
P2 = 0
for y in range(0, len(data)): # idea from u/Sourish17 (reddit)
    for x in range(0, len(data)):
        if (x, y) in viewed_loop:
            continue
        TMP = 0
        for _ in range(len(data)):
            x -= 1
            if x < 0:
                break
            if viewed_loop.get((x,y)):
                TMP += viewed_loop.get((x, y)) in '|JL'
        P2 += TMP % 2

print(f"Part 2: {P2} took {time.time() - t:.4f}s")

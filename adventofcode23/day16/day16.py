"""
Advent of code 2023 - Day 16 - Part 1 & 2
https://adventofcode.com/2023/day/16
"""

import os
import time
import sys
path = os.path.dirname(os.path.realpath(__file__))
FILE = path + "/data.txt"
sys.setrecursionlimit(4000)


with open(FILE, "r", encoding="utf-8") as f:
    data = f.read().splitlines()

ENER = set()

TILES = {}

for i, l in enumerate(data):
    for j, char in enumerate(l):
        if char != '.':
            TILES[(i, j)] = char


N, S, E, W = (-1, 0), (1, 0), (0, 1), (0, -1)
L_LINE = len(data[0])
L_COL = len(data)


def move(pos, direction):
    """Move the light beam from the position and direction
    
    Arguments:
        pos {tuple} -- starting position
        direction {tuple} -- starting direction"""
    if pos[0] < 0 or pos[0] >= L_LINE or pos[1] < 0 or pos[1] >= L_COL or (pos, direction) in ENER:
        return False
    ENER.add((pos, direction))
    if pos in TILES:
        if TILES[pos] == "|":
            if direction in [E, W]:
                direction = N
                move((pos[0] + direction[0], pos[1] + direction[1]), N)
                direction = S
                move((pos[0] + direction[0], pos[1] + direction[1]), S)
            else:
                move((pos[0] + direction[0], pos[1] + direction[1]), direction)
        elif TILES[pos] == "-":
            if direction in [N, S]:
                direction = E
                move((pos[0] + direction[0], pos[1] + direction[1]), E)
                direction = W
                move((pos[0] + direction[0], pos[1] + direction[1]), W)
            else:
                move((pos[0] + direction[0], pos[1] + direction[1]), direction)
        elif TILES[pos] == "\\":
            direction = (direction[1], direction[0])
            move((pos[0] + direction[0], pos[1] + direction[1]), direction)
        elif TILES[pos] == "/":
            direction = (-direction[1], -direction[0])
            move((pos[0] + direction[0], pos[1] + direction[1]), direction)
    else:
        move((pos[0] + direction[0], pos[1] + direction[1]), direction)





def start_move(pos : tuple, direction : tuple):
    """Start the light beam from the position and direction and return the number of tiles visited
    
    Arguments:
        pos {tuple} -- starting position
        direction {tuple} -- starting direction
        
    Returns:
        int -- number of tiles visited"""
    ENER.clear()
    move(pos, direction)
    return(len({pos for (pos, _) in ENER}))


tp1 = time.time()

print(f"Part 1: {start_move((0, 0), E)} in {time.time() - tp1:.4f}s")


tp2 = time.time()


def part2():
    """Part 2"""
    p2 = []
    for line in range(L_COL):
        p2.append(start_move((line, 0), E))
        p2.append(start_move((line, L_LINE-1), W))
    for col in range(L_LINE):
        p2.append(start_move((0, col), S))
        p2.append(start_move((L_COL-1, col), N))
    return max(p2)

print(f"Part 2: {part2()} in {time.time() - tp2:.4f}s")

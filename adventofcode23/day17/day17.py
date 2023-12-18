"""
Advent of code 2023 - Day 17 - Part 1 & 2
https://adventofcode.com/2023/day/17
"""

import os
import time
import heapq
path = os.path.dirname(os.path.realpath(__file__))
FILE = path + "/data.txt"



with open(FILE, "r", encoding="utf-8") as f:
    data = f.read().splitlines()
for ind,l in enumerate(data):
    data[ind] = [int(x) for x in l]

pond = {}

for i, l in enumerate(data):
    for j, x in enumerate(l):
        pond[(i,j)] = x

N,S,E,W = (0,1), (0,-1), (1,0), (-1,0)

def pathfind(start, end, part=1):
    """Find the shortest path from start to end.
    part 1: 1-3 steps
    part 2: 4-10 steps
    """
    if part == 1:
        mini, maxi = 1, 3
    elif part == 2:
        mini, maxi = 4, 10
    queue = [(0, *start, 0, 0)]
    viewed = set()
    while queue:
        heat, curr_x, curr_y, px, py = heapq.heappop(queue)
        if (curr_x, curr_y) == end:
            return heat
        if (curr_x, curr_y, px, py) in viewed:
            continue
        viewed.add((curr_x, curr_y, px, py))
        for dx, dy in {E, N, W, S} - {(px, py), (-px, -py)}:
            a, b, h = curr_x, curr_y, heat
            for _ in range(1, maxi + 1):
                a, b = a + dx, b + dy
                if (a, b) in pond:
                    h += pond[a, b]
                    if _ >= mini:
                        heapq.heappush(queue, (h, a, b, dx, dy))


t1 = time.time()
print("Part1 : ", pathfind((0, 0), max(pond), 1))
print(f"Part 1 : {time.time() - t1:.4f} seconds")

t2 = time.time()
print("Part2 : ", pathfind((0, 0), max(pond), 2))
print(f"Part 2 : {time.time() - t2:.4f} seconds")

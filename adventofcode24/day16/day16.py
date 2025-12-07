import os
import time
import heapq

start = time.time()
path = os.path.dirname(os.path.realpath(__file__))
file = path + "/data.txt"
with open(file, encoding="utf-8") as f:
    data = []
    data = f.read().splitlines()

reindeer = [
    (i, j) for i, line in enumerate(data) for j, char in enumerate(line) if char == "S"
][0]

end = [
    (i, j) for i, line in enumerate(data) for j, char in enumerate(line) if char == "E"
][0]


grid = [[c for c in line] for line in data]

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

r_dir = (-1, 0)  # starting direction

# move is 1 point, and rotate is 1000 points, find the path with the least points


def print_grid(grid, path):
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if (j, i) in path:
                print("X", end="")
            else:
                print(char, end="")
        print()


def dijkstra(start, end, grid, r_dir):
    q = [
        (0, start[0], start[1], r_dir[0], r_dir[1], {(start[0], start[1])})
    ]  # cost, x, y, dx, dy, path
    seen = set()
    while len(q) > 0:
        d, x, y, dx, dy, path = heapq.heappop(q)
        if (x, y) in seen:
            continue
        seen.add((x, y))

        if (x, y) == end:
            return d, path

        for ddx, ddy in dirs:
            if ddx == -dx and ddy == -dy:
                continue
            nx, ny = x + ddx, y + ddy
            is_straight = abs(ddx) == abs(dx) and abs(ddy) == abs(dy)
            cost = 1
            if not is_straight:
                cost += 1000

            if grid[ny][nx] == "#" or (nx, ny) in seen:
                continue

            new_path = path.copy()
            new_path.add((nx, ny))
            heapq.heappush(q, (d + cost, nx, ny, ddx, ddy, new_path))

    return None, None


print(dijkstra(reindeer, end, grid, r_dir)[0])

print_grid(grid, dijkstra(reindeer, end, grid, r_dir)[1])

print("---------")

# Part 2

"""
Now that you know what the best paths look like, you can figure out the best spot to sit.

Every non-wall tile (S, ., or E) is equipped with places to sit along the edges of the tile. While determining which of these tiles would be the best spot to sit depends on a whole bunch of factors (how comfortable the seats are, how far away the bathrooms are, whether there's a pillar blocking your view, etc.), the most important factor is whether the tile is on one of the best paths through the maze. If you sit somewhere else, you'd miss all the action!

So, you'll need to determine which tiles are part of any best path through the maze, including the S and E tiles.
"""

# The best path is the one with the least points, so we can use the same function to find the best path

"""
Example:

###############
#.......#....E#
#.#.###.#.###^#
#.....#.#...#^#
#.###.#####.#^#
#.#.#.......#^#
#.#.#####.###^#
#..>>>>>>>>v#^#
###^#.#####v#^#
#>>^#.....#v#^#
#^#.#.###.#v#^#
#^....#...#v#^#
#^###.#.#.#v#^#
#S..#.....#>>^#
###############

The best path size : 7036

###############
#.......#....O#
#.#.###.#.###O#
#.....#.#...#O#
#.###.#####.#O#
#.#.#.......#O#
#.#.#####.###O#
#..OOOOOOOOO#O#
###O#O#####O#O#
#OOO#O....#O#O#
#O#O#O###.#O#O#
#OOOOO#...#O#O#
#O###.#.#.#O#O#
#O..#.....#OOO#
###############

"""

import networkx as nx

G = nx.Graph()

for i, row in enumerate(grid):
    for j, char in enumerate(row):
        if char != "#":
            G.add_node((i, j))

for i, row in enumerate(grid):
    for j, char in enumerate(row):
        if char != "#":
            for dx, dy in dirs:
                nx, ny = i + dx, j + dy
                if grid[ny][nx] != "#":
                    G.add_edge((i, j), (nx, ny))

path = dijkstra(reindeer, end, grid, r_dir)[1]

for i, row in enumerate(grid):
    for j, char in enumerate(row):
        if char != "#" and (i, j) not in path:
            G.remove_node((i, j))

print(len(path))

print("Time taken: " + str(round(time.time() - start, 3)) + "s")

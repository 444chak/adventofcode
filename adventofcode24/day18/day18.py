import os
import time

start = time.time()
path = os.path.dirname(os.path.realpath(__file__))
file = path + "/data.txt"
with open(file, encoding="utf-8") as f:
    data = []
    data = f.read().splitlines()

data = [tuple(map(int, x.split(","))) for x in data]


LEN = 70 + 1
BYTES = 1024

grid = [["." for i in range(LEN)] for j in range(LEN)]


def print_grid():
    for i in range(LEN):
        for j in range(LEN):
            print(grid[i][j], end="")
        print()


for i in range(BYTES):
    grid[data[i][1]][data[i][0]] = "#"


def dijkstra(grid, start, end):
    queue = [(0, start)]
    visited = set()
    while queue:
        cost, pos = queue.pop(0)
        if pos in visited:
            continue
        visited.add(pos)
        if pos == end:
            return cost
        x, y = pos
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < LEN and 0 <= ny < LEN and grid[ny][nx] == ".":
                queue.append((cost + 1, (nx, ny)))
    return float("inf")


print(f"Part 1: {dijkstra(grid, (0, 0), (LEN - 1, LEN - 1))}")

# Part 2


for i in range(BYTES, len(data)):
    grid[data[i][1]][data[i][0]] = "#"
    dij = dijkstra(grid, (0, 0), (LEN - 1, LEN - 1))
    if dij == float("inf"):
        print(f"Part 2: {data[i][0]},{data[i][1]}")
        break


print("Time taken: " + str(round(time.time() - start, 3)) + "s")

import os
import time
from collections import deque

start_time = time.time()
path = os.path.dirname(os.path.realpath(__file__))
file = path + "/data.txt"
with open(file, encoding="utf-8") as f:
    data = []
    data = f.read().splitlines()


"""
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""

start = [
    (x, y) for x in range(len(data)) for y in range(len(data[x])) if data[x][y] == "S"
][0]
end = [
    (x, y) for x in range(len(data)) for y in range(len(data[x])) if data[x][y] == "E"
][0]

pos = start
step = 0
cheat = {start: 0}

print(start, end, cheat)

queue = deque([(start, 0)])
visited = set()
visited.add(start)

while queue:
    pos, step = queue.popleft()
    if pos == end:
        break
    i, j = pos
    for di, dj in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
        newi, newj = i + di, j + dj
        new_pos = (newi, newj)
        if new_pos not in visited and data[newi][newj] in "SE.":
            visited.add(new_pos)
            queue.append((new_pos, step + 1))
            cheat[new_pos] = step + 1


THRESHOLD = 100

print(
    sum(
        1
        for (i, j), step in cheat.items()
        for di, dj in [[-1, 0], [0, -1], [0, 1], [1, 0]]
        if (
            (i + di, j + dj) not in cheat
            and (i + 2 * di, j + 2 * dj) in cheat
            and cheat[(i + 2 * di, j + 2 * dj)] - step >= THRESHOLD + 2
        )
    )
)


def cheat_endpoints(coords):
    i, j = coords
    output = set()
    for di in range(-20, 21):
        for dj in range(-20, 21):
            if abs(di) + abs(dj) <= 20:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(data) and 0 <= nj < len(data[0]) and (ni, nj) in cheat:
                    output.add((ni, nj))
    return output


print(
    sum(
        1
        for coords, step in cheat.items()
        for othercoords in cheat_endpoints(coords)
        if cheat[othercoords]
        - step
        - (abs(coords[0] - othercoords[0]) + abs(coords[1] - othercoords[1]))
        >= THRESHOLD
    )
)
print("Time taken: " + str(round(time.time() - start_time, 3)) + "s")

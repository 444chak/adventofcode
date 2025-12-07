import os

# get path of the file
path = os.path.dirname(os.path.realpath(__file__))
FILE = path + "/data.txt"

with open(FILE, "r", encoding="utf-8") as f:
    data = f.read().splitlines()

# Part 1

guard = (0, 0)
U,D,L,R = (-1, 0), (1, 0), (0, -1), (0, 1)
g_dir = U
obstacles = []
larg, long = len(data), len(data[0])

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "^":
            guard = (i, j)
        elif data[i][j] == "#":
            obstacles.append((i, j))

        


def in_area(x, y):
    return 0 <= x <= larg and 0 <= y <= long

p1 = 0

def show_map(positions=None):
    for i in range(larg):
        for j in range(long):
            if (i, j) == guard:
                print("G", end="")
            elif (i, j) in obstacles:
                print("#", end="")
            elif positions is not None and (i, j) in positions:
                print("o", end="")
            else:
                print(".", end="")
        print()

positions = set()

while in_area(guard[0] + g_dir[0], guard[1] + g_dir[1]):
    positions.add(guard)
    if (guard[0] + g_dir[0], guard[1] + g_dir[1]) in obstacles:
        if g_dir == U:
            g_dir = R
        elif g_dir == R:
            g_dir = D
        elif g_dir == D:
            g_dir = L
        elif g_dir == L:
            g_dir = U
    else:
        guard = (guard[0] + g_dir[0], guard[1] + g_dir[1])

print(len(positions))



# Part 2

p1_positions = positions.copy()
empty = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "^":
            guard = (i, j)
            start = (i, j)
        if data[i][j] == ".":
            empty.append((i, j))

positions = set()

g_dir = U

# obstacles.append((6,3))
print(guard)

show_map(positions=p1_positions)

def has_loop(loop, guard, g_dir):

    if len(loop) < 4:
        return False

    if loop[-1] == loop[0]:
        return True

    if loop[-1] == loop[1]:
        return False

    if loop[-1] == loop[2]:
        return False

    if loop[-1] == loop[3]:
        return False

    return False


def try_loop(guard=guard, g_dir=g_dir, start=start):
    counter = 0
    while in_area(guard[0] + g_dir[0], guard[1] + g_dir[1]):
        positions.add(guard)
        counter += 1
        if counter == 10000:
            return True
        if (guard[0] + g_dir[0], guard[1] + g_dir[1]) in obstacles:
            if g_dir == U:
                g_dir = R
            elif g_dir == R:
                g_dir = D
            elif g_dir == D:
                g_dir = L
            elif g_dir == L:
                g_dir = U
            
        else:
            guard = (guard[0] + g_dir[0], guard[1] + g_dir[1])
    return False
import time

time_start = time.perf_counter()

p2 = 0
for test in p1_positions:
    obstacles.append(test)
    if try_loop():
        p2 += 1
    obstacles.remove(test)
print(p2)
print(f'Solved in {time.perf_counter()-time_start:.5f} Sec.')
# 1957
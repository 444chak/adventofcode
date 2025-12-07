import os
from itertools import combinations
path = os.path.dirname(os.path.realpath(__file__))
FILE = os.path.join(path, "data.txt")
# Read data from file
with open(FILE, "r", encoding="utf-8") as f:
    data = f.read().splitlines()

print(data)


# ............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............

# The signal only applies its nefarious effect at specific antinodes based on the resonant frequencies of the antennas. In particular, an antinode occurs at any point that is perfectly in line with two antennas of the same frequency - but only when one of the antennas is twice as far away as the other. This means that for any pair of antennas with the same frequency, there are two antinodes, one on either side of them.

# ......#....#
# ...#....0...
# ....#0....#.
# ..#....0....
# ....0....#..
# .#....A.....
# ...#........
# #......#....
# ........A...
# .........A..
# ..........#.
# ..........#.

# Calculate the impact of the signal. How many unique locations within the bounds of the map contain an antinode?

freq = {}

def get_antinode(x1, y1, x2, y2):
    x_diff = x1 - x2
    y_diff = y1 - y2
    pot_x1 = x1 + x_diff
    pot_y1 = y1 + y_diff
    pot_x2 = x2 - x_diff
    pot_y2 = y2 - y_diff
    return (pot_x1, pot_y1), (pot_x2, pot_y2)

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] != '.':
            if data[i][j] not in freq:
                freq[data[i][j]] = []
            freq[data[i][j]].append((i, j))


larg = len(data)
long = len(data[0])

p1 = 0

antinodes = set()


for k,v in freq.items():
    for a, b in combinations(v, 2):
        x1, y1 = a
        x2, y2 = b
        antinode1, antinode2 = get_antinode(x1, y1, x2, y2)
        if antinode1:
            antinodes.add(antinode1)
        if antinode2:
            antinodes.add(antinode2)
        
for anti in antinodes:
    x, y = anti
    if 0 <= x < long and 0 <= y < larg:
        p1 += 1

print(p1)

# (1, 8), (2, 5)
# (2, 5), (3, 7)
# (3, 7), (4, 4)
# (1, 8),  (4, 4)
# (2, 5), (4, 4)
# (1, 8), (3, 7)

def get_all_antinodes(x1, y1, x2, y2):
    """After updating your model, it turns out that an antinode occurs at any grid position exactly in line with at least two antennas of the same frequency, regardless of distance. This means that some of the new antinodes will occur at the position of each antenna (unless that antenna is the only one of its frequency)."""
    x = x1
    y = y1
    while 0 <= x < long and 0 <= y < larg:
        yield (x, y)
        x += x2 - x1
        y += y2 - y1
    x = x2
    y = y2
    while 0 <= x < long and 0 <= y < larg:
        yield (x, y)
        x += x1 - x2
        y += y1 - y2
        



antinodes = set()

for k,v in freq.items():
    for a, b in combinations(v, 2):
        x1, y1 = a
        x2, y2 = b
        antinodes.update(get_all_antinodes(x1, y1, x2, y2))

p2 = 0

print(len(antinodes))   
import os
import time

start = time.time()

path = os.path.dirname(os.path.realpath(__file__))
file = path + "/data.txt"
with open(file, encoding="utf-8") as f:
    data = []
    data = f.read().splitlines()

parcels = {}  # type : [area, perimeter]

# RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
# VVRCCCJFFF
# VVVVCJJCFE
# VVIVCCJJEE
# VVIIICJJEE
# MIIIIIJJEE
# MIIISIJEEE
# MMMISSJEEE

# AAAA
# BBCD
# BBCC
# EEEC

print(data)


def get_neighbours(x, y):
    neighbours = []
    if x > 0:
        neighbours.append((x - 1, y))
    if x < len(data[0]) - 1:
        neighbours.append((x + 1, y))
    if y > 0:
        neighbours.append((x, y - 1))
    if y < len(data) - 1:
        neighbours.append((x, y + 1))
    return neighbours


def get_area(x, y, data):
    area = 0
    permimeter = 0
    plant = data[y][x]
    positions = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == data[y][x]:
                area += 1
                positions.append((j, i))

    # each case has 4 sides, but if a side is shared with another parcel, it is not counted

    # list of neighbourshoods, a neighbourhood is a list of coordinates of positions that are connected directly

    nb_of_alone = 0
    for pos in positions:
        x, y = pos
        neighbours = get_neighbours(x, y)
        alone = True
        for n in neighbours:
            if data[n[1]][n[0]] == plant:
                alone = False
                break
        if alone:
            nb_of_alone += 1

    for pos in positions:
        x, y = pos
        permimeter += 4
        neighbours = get_neighbours(x, y)
        for n in neighbours:
            if data[n[1]][n[0]] == plant:
                permimeter -= 1

    if nb_of_alone != 0:
        permimeter /= nb_of_alone

    return area, permimeter


for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] not in parcels:
            parcels[data[i][j]] = get_area(j, i, data)

print(parcels)


def solve(dict):
    p1 = 0
    for _, v in dict.items():
        p1 += v[0] * v[1]
    return p1


print(f"Part 1: {solve(parcels)}")

regions = []

points = []

for i in range(len(data)):
    for j in range(len(data[i])):
        points.append((j, i, data[i][j]))

# [(0, 0, 'R'), (1, 0, 'R'), (2, 0, 'R'), (3, 0, 'R'), (4, 0, 'I'), (5, 0, 'I'), (6, 0, 'C'), (7, 0, 'C'), (8, 0, 'F'), (9, 0, 'F'), (0, 1, 'R'), (1, 1, 'R'), (2, 1, 'R'), (3, 1, 'R'), (4, 1, 'I'), (5, 1, 'I'), (6, 1, 'C'), (7, 1, 'C'), (8, 1, 'C'), (9, 1, 'F'), (0, 2, 'V'), (1, 2, 'V'), (2, 2, 'R'), (3, 2, 'R'), (4, 2, 'R'), (5, 2, 'C'), (6, 2, 'C'), (7, 2, 'F'), (8, 2, 'F'), (9, 2, 'F'), (0, 3, 'V'), (1, 3, 'V'), (2, 3, 'R'), (3, 3, 'C'), (4, 3, 'C'), (5, 3, 'C'), (6, 3, 'J'), (7, 3, 'F'), (8, 3, 'F'), (9, 3, 'F'), (0, 4, 'V'), (1, 4, 'V'), (2, 4, 'V'), (3, 4, 'V'), (4, 4, 'C'), (5, 4, 'J'), (6, 4, 'J'), (7, 4, 'C'), (8, 4, 'F'), (9, 4, 'E'), (0, 5, 'V'), (1, 5, 'V'), (2, 5, 'I'), (3, 5, 'V'), (4, 5, 'C'), (5, 5, 'C'), (6, 5, 'J'), (7, 5, 'J'), (8, 5, 'E'), (9, 5, 'E'), (0, 6, 'V'), (1, 6, 'V'), (2, 6, 'I'), (3, 6, 'I'), (4, 6, 'I'), (5, 6, 'C'), (6, 6, 'J'), (7, 6, 'J'), (8, 6, 'E'), (9, 6, 'E'), (0, 7, 'M'), (1, 7, 'I'), (2, 7, 'I'), (3, 7, 'I'), (4, 7, 'I'), (5, 7, 'I'), (6, 7, 'J'), (7, 7, 'J'), (8, 7, 'E'), (9, 7, 'E'), (0, 8, 'M'), (1, 8, 'I'), (2, 8, 'I'), (3, 8, 'I'), (4, 8, 'S'), (5, 8, 'I'), (6, 8, 'J'), (7, 8, 'E'), (8, 8, 'E'), (9, 8, 'E'), (0, 9, 'M'), (1, 9, 'M'), (2, 9, 'M'), (3, 9, 'I'), (4, 9, 'S'), (5, 9, 'S'), (6, 9, 'J'), (7, 9, 'E'), (8, 9, 'E'), (9, 9, 'E')]

# get regions of connected parcels


def get_neighbors(point, points_dict):
    """Retourne les voisins valides d'un point ayant le même type"""
    x, y, type_point = point
    neighbors = []
    # Vérifier les 4 directions (haut, bas, gauche, droite)
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_x, new_y = x + dx, y + dy
        neighbor = (new_x, new_y)
        if neighbor in points_dict and points_dict[neighbor] == type_point:
            neighbors.append((new_x, new_y, type_point))
    return neighbors


def find_connected_regions(points):
    """Trouve toutes les régions connexes"""
    # Créer un dictionnaire pour un accès plus rapide
    points_dict = {(x, y): type_point for x, y, type_point in points}

    # Ensemble pour marquer les points visités
    visited = set()
    regions = []

    def dfs(point, current_region):
        """Parcours en profondeur pour trouver une région connexe"""
        visited.add((point[0], point[1]))
        current_region.append(point)

        for neighbor in get_neighbors(point, points_dict):
            if (neighbor[0], neighbor[1]) not in visited:
                dfs(neighbor, current_region)

    # Parcourir tous les points
    for point in points:
        if (point[0], point[1]) not in visited:
            current_region = []
            dfs(point, current_region)
            regions.append(current_region)

    return regions


regions = find_connected_regions(points)

p1 = 0

for i, region in enumerate(regions):
    print(f"Région {i + 1} ({region[0][2]}):")
    print(f"  Points: {len(region)}")
    print(f"  Coordonnées: {[(x, y) for x, y, _ in region]}\n")


for region in regions:
    area = len(region)
    perimeter = 0
    for x, y, _ in region:
        neighbors = get_neighbors((x, y, _), {(x, y): _ for x, y, _ in region})
        perimeter += 4 - len(neighbors)
    print(f"Area: {area}, Perimeter: {perimeter}")
    p1 += area * perimeter


print(f"Part 1: {p1}")

print("----------------------------")

# instead of using the perimeter to calculate the price, you need to use the number of sides each region has. Each straight section of fence counts as a side, regardless of how long it is.


def count_sides(region: set[tuple[int, int]]) -> int:
    parcel = set()
    sides = 0

    for x, y in sorted(region, key=lambda x: tuple(reversed(x))):
        for ax, ay, side in (
            (x - 1, y, "L"),
            (x, y - 1, "T"),
            (x + 1, y, "R"),
            (x, y + 1, "B"),
        ):
            if (ax, ay) not in region:
                dx, dy = int(ax == x), int(ay == y)
                if (x - dx, y - dy, side) not in parcel and (
                    x - dx,
                    y - dy,
                    side,
                ) not in parcel:
                    sides += 1
                parcel.add((x, y, side))

    return sides


p2 = 0

for i, region in enumerate(regions):
    print(f"Région {i + 1} ({region[0][2]}):")
    print(f"  Points: {len(region)}")
    print(f"  Coordonnées: {[(x, y) for x, y, _ in region]}\n")
    print(count_sides(set((x, y) for x, y, _ in region)))

    p2 += (count_sides(set((x, y) for x, y, _ in region))) * len(region)

print(f"Part 2: {p2}")

print(f"Time: {time.time() - start}")

from aoc_utils.aoc_utils import Timer, get_data, print_solution

data = get_data()
timer = Timer()

starts = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "0":
            starts.append((j, i))


def get_neighbors(x, y):
    neighbors = []
    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if 0 <= x + i < len(data[0]) and 0 <= y + j < len(data):
            neighbors.append((x + i, y + j))
    return neighbors


def show_path(data, path):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if (j, i) in path:
                print(data[i][j], end="")
            else:
                print(".", end="")
        print()


def paths_of_1_increment(x, y, path, paths):
    """Count how many paths are there with 1 increment from start to "9"."""
    if data[y][x] == "9":
        paths.append(path)
        return
    neighbors = get_neighbors(x, y)
    for neighbor in neighbors:
        if neighbor not in path:
            if int(data[neighbor[1]][neighbor[0]]) == int(data[y][x]) + 1:
                paths_of_1_increment(neighbor[0], neighbor[1], path + [neighbor], paths)


def counts_paths(paths):
    """A path count for any different 9 at the end."""
    counts = set()
    for path in paths:
        counts.add(path[-1])
    return len(counts)


p1 = 0
p2 = 0
for start in starts:
    paths = []
    paths_of_1_increment(start[0], start[1], [start], paths)
    p1 += counts_paths(paths)
    p2 += len(paths)


print_solution(p1, p2, timer)

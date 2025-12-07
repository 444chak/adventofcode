import os
import itertools
path = os.path.dirname(os.path.realpath(__file__))
FILE = os.path.join(path, "data.txt")
# Read data from file
with open(FILE, "r", encoding="utf-8") as f:
    data = f.read().splitlines()

disk = []
disk_2 = []
id = 0
for index, k in enumerate(data[0]):
    if index % 2 != 0:
        if int(k) != 0:
            disk_2.append([None] * int(k))
        for _ in range(int(k)):
            disk.append(None)
    else:
        disk_2.append([id] * int(k))
        for _ in range(int(k)):
            disk.append(id)
        id += 1


def print_disk(disk):
    # neasted disk
    for index, k in enumerate(disk):
        if index % 100 == 0:
            print()
        if k == None:
            print(".", end="")
        else:
            print(k, end="")
    print()

print_disk(disk)
original_disk = disk.copy()
new_disk = []


new_disk_2 = []

for index, k in enumerate(disk):
    if k != None:        
        new_disk.append(k)
    if k == None:
        while disk[-1] == None:
            disk.pop()
        new_disk.append(disk.pop())


p1 = sum([i * int(k) for i, k in enumerate(new_disk)])

print(new_disk)

print(p1)
# 6330095022244
print("--------------")

disk = original_disk.copy()

def get_first_free_space(disk):
    free_size = 0
    free_start = 0
    for index, k in enumerate(disk):
        if k == None:
            free_size += 1
        else:
            if free_size > 0:
                return free_start, free_size
            free_start = index + 1
            free_size = 0

    return free_start, free_size

def get_all_free_space(disk):
    free_size = 0
    free_start = 0
    free_spaces = []
    for index, k in enumerate(disk):
        if k == None:
            free_size += 1
        else:
            if free_size > 0:
                free_spaces.append((free_start, free_size))
            free_start = index + 1
            free_size = 0

    return free_spaces

for f in reversed(disk_2):
    frees = get_all_free_space(disk)

    for start, size in frees:
        if size >= len(f) and f[0] != None and start <= disk.index(f[0]):
            # disk = list(filter(lambda x: x != f[0], disk))
            disk = [None if x == f[0] else x for x in disk]

            for index, k in enumerate(f):
                disk[start + index] = k
            disk_2.remove(f)
            break

# 00992111777.44.333....5555.6666.....8888..
# 00992111777.44.333....5555.6666.....8888..
p2 = 0
for index, k in enumerate(disk):
    if k != None:
        p2 += index * k

print(p2)

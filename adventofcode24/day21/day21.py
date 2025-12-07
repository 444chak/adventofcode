import os
import time
from collections import Counter

start_time = time.time()
path = os.path.dirname(os.path.realpath(__file__))
file = path + "/data.txt"

# Lecture des codes
with open(file, encoding="utf-8") as f:
    codes = f.read().splitlines()

# Définition des pavés
numpad = {
    "A": (3, 2),
    "0": (3, 1),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
}

keypad = {"A": (0, 2), "^": (0, 1), "<": (1, 0), "v": (1, 1), ">": (1, 2)}


def get_pos_num(num):
    return numpad[num]


def get_pos_key(key):
    return keypad[key]


import random


def best_path(start, end):
    path = []
    x, y = start
    x2, y2 = end

    first_while = random.choice(["h", "v"])

    if first_while == "h":
        while x != x2:
            if x < x2:
                path.append("v")
                x += 1
            else:
                path.append("^")
                x -= 1

        while y != y2:
            if y < y2:
                path.append(">")
                y += 1
            else:
                path.append("<")
                y -= 1
    else:
        while y != y2:
            if y < y2:
                path.append(">")
                y += 1
            else:
                path.append("<")
                y -= 1

        while x != x2:
            if x < x2:
                path.append("v")
                x += 1
            else:
                path.append("^")
                x -= 1

    # while x != x2:
    #     if x < x2:
    #         path.append("v")
    #         x += 1
    #     else:
    #         path.append("^")
    #         x -= 1

    # while y != y2:
    #     if y < y2:
    #         path.append(">")
    #         y += 1
    #     else:
    #         path.append("<")
    #         y -= 1

    return path


def process(code):
    postest = numpad["A"]
    test_path = []
    for k in code:
        pos = get_pos_num(k)
        test_path += best_path(postest, pos)
        postest = pos
        test_path += ["A"]

    path2 = []
    pos2 = keypad["A"]
    for k in test_path:
        pos = get_pos_key(k)
        path2 += best_path(pos2, pos)
        pos2 = pos
        path2 += ["A"]

    path3 = []
    pos3 = keypad["A"]
    for k in path2:
        pos = get_pos_key(k)
        path3 += best_path(pos3, pos)
        pos3 = pos
        path3 += ["A"]

    # print(f"{len(path3)} * {int(code.replace('A', ''))}")
    # print("".join(path3))
    # print()

    return len(path3) * int(code.replace("A", ""))


p1 = 0
for i in codes:
    p1 += process(i)
print("Part 1: " + str(p1))

list_p1 = []
for i in range(100):
    p = 0
    for j in codes:
        p += process(j)
    list_p1.append(p)

print(set(list_p1))

for i, p1 in enumerate(set(list_p1)):
    print(i, p1)


# <v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
# v<<A^>>AvA^Av<<A^>>AAv<A<A^>>AA<Av>AA^Av<A^>AA<A>Av<A<A^>>AAA<Av>A^A

"""
    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |


219254
"""

"""
Advent of code 2023 - Day 11 - Part 1 & 2
https://adventofcode.com/2023/day/11
"""

import os
import time

path = os.path.dirname(os.path.realpath(__file__))
FILE = path + "/data.txt"


with open(FILE, "r", encoding="utf-8") as f:
    data = []
    data = f.read().splitlines()

def univers_expansion(input_data):
    """
    return empty rows & columns
    """
    empty_rows = []
    empty_columns = []
    for y, row in enumerate(input_data):
        if row == "." * len(row):
            empty_rows.append(y)

    for x in range(len(input_data[0])):
        if "".join([input_data[y][x] for y in range(len(input_data))]) == "." * len(input_data):
            empty_columns.append(x)

    return empty_rows, empty_columns

def count_empty(n, empty_list, exp):
    """
    return the number of empty rows or columns before n
    """
    count = 0
    for i in empty_list:
        if i < n:
            count += (exp - 1)
    return count

def galaxies_list(input_data, exp):
    """
    return a list of galaxies
    
    :param input_data: list of rows
    :param exp: expansion factor

    :return: a list of galaxies
    """
    galaxy = 0
    galaxy_list = {}
    for y, row in enumerate(input_data):
        for x, char in enumerate(row):
            if char == "#":
                galaxy += 1
                galaxy_list[galaxy] = (x + count_empty(x, EC, exp), y + count_empty(y, ER, exp))
    return galaxy_list



def path_lenght(g1, g2, glist):
    """
    return the path lenght between 2 galaxy
    """
    return abs(glist[g1][0] - glist[g2][0]) + abs(glist[g1][1] - glist[g2][1])


def solve(input_data, exp):
    """
    return the total lenght of all the paths
    
    :param input_data: list of rows
    :param exp: expansion factor
    """
    glist = galaxies_list(input_data, exp)
    total = 0
    for i in range(1, len(glist)+1):
        for j in range(i+1, len(glist)+1):
            total += path_lenght(i, j, glist)
    return total

ER, EC = univers_expansion(data)



# ------------------ PART 1 ------------------ #
t = time.time()
p1 = solve(data, 2)
print(f"Part 1: {p1} took {time.time() - t:.4f}s")

# ------------------ PART 2 ------------------ #
t = time.time()
p2 = solve(data, 1000000)
print(f"Part 2: {p2} took {time.time() - t:.4f}s")

# pylint: disable=W0105
"""
Advent of code 2023 - Day 13 - Part 1 & 2
https://adventofcode.com/2023/day/13
"""

import os
import time

path = os.path.dirname(os.path.realpath(__file__))
FILE = path + "/data.txt"


with open(FILE, "r", encoding="utf-8") as f:
    data = f.read()

def reflect_vert(pattern, old = None):
    """
    Check if pattern is vertical mirror"""
    prev_cols = []
    prev_cols.append([pattern[y][0] for y in range(len(pattern))])
    for x in range(1, len(pattern[0])):
        col = [pattern[y][x] for y in range(len(pattern))]
        if col == prev_cols[-1]:
            # check if symetry
            rest = len(pattern[0]) - x
            isok = True
            for i in range(1,rest):
                col_to_check = [pattern[y][len(pattern[0]) - rest + i] for y in range(len(pattern))]
                try:
                    if col_to_check != prev_cols[-(i+1)]:
                        isok = False
                        break
                except IndexError:
                    pass

            if old and isok:
                if x == old:
                    isok = False
            if isok:
                return x
        prev_cols.append(col)
    return False

def reflect_hor(pattern, old = None):
    """
    Check if pattern is horizontal mirror"""
    prev_rows = []
    prev_rows.append(pattern[0])
    for y,row in enumerate(pattern[1:]):
        if row == prev_rows[-1]:
            # check if symetry
            rest = len(pattern) - y
            isok = True
            for i in range(y+2,rest+y):
                row_to_check = pattern[i]
                try:
                    if row_to_check != prev_rows[(len(prev_rows) - i)-1]:
                        isok = False
                        break
                except IndexError:
                    pass
            if old and isok:
                if (len(prev_rows) * 100) == old:
                    isok = False
            if isok:
                return len(prev_rows) * 100
        prev_rows.append(row)
    return False

def fnd_reflect(pattern, old = None):
    """Find reflection"""
    if old:
        hor = reflect_hor(pattern, old)
        vert = reflect_vert(pattern, old)
        if hor != old and hor is not False:
            return hor
        if vert != old and vert is not False:
            return vert
    hor = reflect_hor(pattern)
    vert = reflect_vert(pattern)
    if hor:
        return hor
    if vert:
        return vert
    return 0


def get_patterns(input_data):
    """get patterns from string to dict"""
    patterns = {}
    tmp = ""
    ind = 0
    for _,line in enumerate(input_data.splitlines()):
        if line.strip() == "":
            patterns[ind] = tmp
            tmp = ""
            ind += 1
        else:
            tmp += line.strip() + "\n"
    patterns[ind] = tmp
    return patterns

def generate_pattern(pattern):
    """generate pattern list from string"""
    return pattern.splitlines()

def smudge(pattern):
    """generate all possible smudges"""
    for i,c in enumerate(pattern):
        if c != '\n':
            yield pattern[:i]+('.#'[c=='.'])+pattern[i+1:]


def solve(input_data):
    """Solve the problem"""
    t = time.time()
    p1 = 0
    p2 = 0
    for _,pattern in get_patterns(input_data).items():
        rep = 0
        old_rep = fnd_reflect(generate_pattern(pattern))
        p1 += old_rep
        for alt in smudge(pattern):
            reflect = fnd_reflect(generate_pattern(alt), old_rep)
            if reflect != 0 and reflect != old_rep:
                rep = reflect
        if rep == 0:
            rep = fnd_reflect(generate_pattern(pattern))
        p2 += rep

    print("Part 1:",p1)
    print("Part 2:",p2)
    print(f"Time: {time.time() - t:.4f}s")

solve(data)

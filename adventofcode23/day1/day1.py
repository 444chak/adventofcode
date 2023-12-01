"""
Advent of code 2023 - Day 1 - Part 1 & 2
https://adventofcode.com/2023/day/1
"""

import os

# get path of the file
path = os.path.dirname(os.path.realpath(__file__))
FILE = path + "/data.txt"


def part1():
    """
    Part 1
    """
    with open(FILE, encoding='utf-8') as f:
        total = 0
        for i in f.readlines():
            nb = []
            for j in i:
                if j.isdigit():
                    # concatenate the digits
                    nb.append(j)

            nb = nb[0] + nb[-1]
            total += int(nb)

    print(total)

part1()


# bonus
print(sum(int(nb[0] + nb[-1]) for nb in [list(filter(str.isdigit, i)) for i in open(FILE, encoding='utf-8')]))


numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
}

def part2():
    """
    Part 2
    """
    with open(FILE, encoding='utf-8') as f:
        total = 0
        for i in f.readlines():
            nb = []
            string = ""
            for j in i:
                if j.isalpha():
                    string += j
                    for k,v in numbers.items():
                        if k in string:
                            nb.append(v)
                            string = string[-1] # most important line
                if j.isdigit():
                    nb.append(j)

            nb = str(nb[0]) + str(nb[-1])
            total += int(nb)

    print(total)

part2()

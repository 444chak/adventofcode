"""
Advent of code 2023 - Day 8 - Part 1 & 2
https://adventofcode.com/2023/day/8
"""

import os
import time
from math import lcm

path = os.path.dirname(os.path.realpath(__file__))
FILE = path + "/data.txt"


with open(FILE, "r", encoding="utf-8") as f:
    data = []
    data = f.read().splitlines()


def parse(input_data):
    """Parse the data and return the rules."""
    rules = {}
    for line in input_data:
        rule = line.split(" = ")
        rules[rule[0]] = rule[1].replace(")", "").replace("(", "").split(", ")
    return rules


def next_in_seq(input_seq, index):
    """Return the next element in the sequence."""
    return seq[index % len(input_seq)]


def part1(input_data, input_seq):
    """Calculate part 1 of the problem."""
    t0 = time.time()
    pos = "AAA"
    steps = 0
    while pos != "ZZZ":
        if next_in_seq(input_seq, steps) == "R":
            pos = input_data[pos][1]
        else:  # L
            pos = input_data[pos][0]
        steps += 1
    return steps, str(time.time() - t0)[:5]


def part2(input_data, input_seq, input_starts):
    """Calculate part 2 of the problem."""
    t0 = time.time()
    for i, key in enumerate(input_starts):
        steps = 0
        while key[-1] != "Z":
            if next_in_seq(input_seq, steps) == "R":
                key = input_data[key][1]
            else:  # L
                key = input_data[key][0]
            steps += 1
        input_starts[i] = steps
    return lcm(*input_starts), str(time.time() - t0)[:5]


seq = data[0]
data = data[2:]
data = parse(data)
starts = [i for i in data if i[-1] == "A"]

p1 = part1(data, seq)
print(f"Part 1: {p1[0]} in {p1[1]}s")
p2 = part2(data, seq, starts)
print(f"Part 2: {p2[0]} in {p2[1]}s")

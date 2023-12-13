"""
Advent of code 2023 - Day 9 - Part 1 & 2
https://adventofcode.com/2023/day/9
"""

import os
import time

path = os.path.dirname(os.path.realpath(__file__))
FILE = path + "/data.txt"


with open(FILE, "r", encoding="utf-8") as f:
    data = []
    data = f.read().splitlines()

for s, line in enumerate(data):
    data[s] = [int(x) for x in line.split(" ")]

def solve(input_data, p2=False):
    """Solve both parts of the problem."""
    t0 = time.time()
    stories = []
    for _, input_line in enumerate(input_data):
        story = []
        story.append(input_line)
        while set(input_line) != {0}:
            nextseq = []
            for j, num in enumerate(input_line):
                if j != 0:
                    nextseq.append(num - input_line[j - 1])
            story.append(nextseq)
            input_line = nextseq

        story.reverse()
        stories.append(story[1:])

    total = 0
    for i, story in enumerate(stories):
        for j, story_line in enumerate(story):
            if j != len(story) - 1:
                if p2:
                    new_value = stories[i][j+1][0] - story_line[0]
                    stories[i][j+1].insert(0, new_value)
                else:
                    new_value = story_line[-1] + stories[i][j+1][-1]
                    stories[i][j+1].append(new_value)

        total += stories[i][-1][0] if p2 else stories[i][-1][-1]


    print(f"Part {2 if p2 else 1}: {total} took {time.time() - t0:.4f}s")


solve(data,p2=False)
solve(data,p2=True)

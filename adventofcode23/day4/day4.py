"""
Advent of code 2023 - Day 3 - Part 1 & 2
https://adventofcode.com/2023/day/3
"""

import os

path = os.path.dirname(os.path.realpath(__file__))
FILE = path + "/data.txt"

POINTS = 0

"""
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

"""

TEST = False

if TEST:
    marge = 8
else:
    marge = 10

def howmuchsame(card):
    overlap = set(card[0]).intersection(*card)
    return overlap,len(overlap)

with open(FILE, "r", encoding="utf-8") as f:
    data = []
    for line in f:
        line = line.strip()[marge:]
        line = line.split(" | ")
        data.append(line)
    for j, card in enumerate(data): 
        for i, number in enumerate(card):
            part = []
            for k in range(0, len(number), 3):
                part.append(int(number[k:k+3].strip()))
            data[j][i] = part


def part1(data):
    points = 0

    # check how much character are the same
    for card in data:
        cardpoints = 0
        for i in range(howmuchsame(card)[1]):
            if i == 0:
                cardpoints += 1
            else:
                cardpoints = cardpoints*2

        points += cardpoints
    print(points)
part1(data)



def part2():
    dictio = {i:1 for i in range(1, len(data) + 1)}
    for i, card in enumerate(data, start=1):
        for j in range(i+1, i+howmuchsame(card)[1]+1):
            dictio[j] = dictio.get(j,0) + dictio[i]
    print(sum(dictio.values()))

part2()
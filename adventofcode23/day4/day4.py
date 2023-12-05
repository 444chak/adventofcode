"""
Advent of code 2023 - Day 4 - Part 1 & 2
https://adventofcode.com/2023/day/4
"""

import os

path = os.path.dirname(os.path.realpath(__file__))
FILE = path + "/data.txt"

POINTS = 0


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
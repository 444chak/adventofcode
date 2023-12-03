"""
Advent of code 2023 - Day 2 - Part 1 & 2
https://adventofcode.com/2023/day/2
"""

import os
import re

# get path of the file
path = os.path.dirname(os.path.realpath(__file__))
FILE = path + "/data.txt"


with open(FILE, 'r', encoding='utf-8') as f:
    data = f.read().split('\n')


for i, d in enumerate(data):
    data[i] = d.split(';')

for i, _ in enumerate(data):
    for j, _ in enumerate(data[i]):
        data[i][j] = data[i][j].split(',')

# delete "Game x: " from each list
for i, _ in enumerate(data):
    for j, _ in enumerate(data[i]):
        for k, _ in enumerate(data[i][j]):
            data[i][j][k] = data[i][j][k].replace('Game ' + str(i+1) + ': ', '')

theory = {
    'red': 12,
    'green': 13,
    'blue': 14
}
RESULT = 0
for i, _ in enumerate(data):
    POSSIBLE = True
    for j, _ in enumerate(data[i]):
        for k, _ in enumerate(data[i][j]):
            for key, val in theory.items():
                if key in data[i][j][k]:
                    # get number of cubes in data (parse int)
                    number = re.findall(r'\d+', data[i][j][k])
                    if int(number[0]) > val:
                        POSSIBLE = False

    if POSSIBLE:
        RESULT += i+1

print(RESULT)

# Part 2
POWERALL = 0
for i, _ in enumerate(data):
    POWER = 0
    mini = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for j, _ in enumerate(data[i]):
        for k, _ in enumerate(data[i][j]):
            for key, val in mini.items():
                if key in data[i][j][k]:
                    number = re.findall(r'\d+', data[i][j][k])
                    if int(number[0]) > val:
                        mini[key] = int(number[0])
    POWER = mini['red'] * mini['green'] * mini['blue']
    POWERALL += POWER

print(POWERALL)

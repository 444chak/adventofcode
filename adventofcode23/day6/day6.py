"""
Advent of code 2023 - Day 6 - Part 1 & 2
https://adventofcode.com/2023/day/6
"""

import os

path = os.path.dirname(os.path.realpath(__file__))
FILE = path + "/data.txt"
"""
Time:      7  15   30
Distance:  9  40  200
"""

with open(FILE, "r", encoding="utf-8") as f:
    data = []
    data = f.read().splitlines()

courses = [] # liste des courses (forme : [temps, distance record])
import re
times = re.split(" +", data[0])
distances = re.split(" +", data[1])
for i in range(1,len(times)):
    courses.append([int(times[i]), int(distances[i])])

print(courses)
    
def course(ms,charge):
    """
    renvoie le temps de charge et le nombre de mm déplacé pour gagner la course à coup sur
    rappel : 1ms de charge = 1mm/ms
    il faut que le temps total (la charge compte) soit inférieur à ms
    :param: ms: temps maximum de la course en ms
    :param: charge: temps de la charge en ms"""
    # temps de charge
    vitesse = charge
    temps_rest = ms
    temps_rest -= charge
    distance = 0
    distance += vitesse * temps_rest
    return distance

total = 0    
for i in range(7):
    tmp = course(7, i)
    if tmp > 9:
        total += 1

print(total)
    
def way_to_win(ms, record):
    total = 0    
    for i in range(ms):
        tmp = course(ms, i)
        if tmp > record:
            total += 1
    return total

print(way_to_win(7, 9))
result = None
for c in courses:
    if result == None:
        result = way_to_win(c[0], c[1])
    else:
        result *= way_to_win(c[0], c[1])

print(result)

# part 2

c = []
c1 = []
for i in data[0]:
    
    if i.isdigit():
        c1.append(int(i))
ctmp = ""
for j in c1:
    ctmp += str(j)

c.append(int(ctmp))

c2 = []
for i in data[1]:
    if i.isdigit():
        c2.append(int(i))

ctmp = ""
for j in c2:
    ctmp += str(j)

c.append(int(ctmp))
    

print(c)
import time
t0 = time.time()
print(way_to_win(c[0], c[1]))
print(time.time() - t0)
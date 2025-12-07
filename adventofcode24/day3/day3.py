



# xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
import os

# get path of the file
path = os.path.dirname(os.path.realpath(__file__))
FILE = path + "/data.txt"

with open(FILE, "r", encoding="utf-8") as f:
    data = f.read().split("\n")


import re

print(data[0])

matches = []
for l in data:
    matches.append(re.findall(r"mul\(\d+,\d+\)", l))
# matches = re.findall(r"mul\(\d+,\d+\)", data[0])

p1 = 0
# [x for xs in xss for x in xs]
matches = [m for ms in matches for m in ms]

for m in matches:
    print(m)
    a, b = re.findall(r"\d+", m)
    p1 += int(a) * int(b)

print(p1)
    
# Part 2

print("----------Part 2----------")

p2 = 0

matches = []
for l in data:
    matches.append(re.findall(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))", l))

matches = [m for ms in matches for m in ms]
enabled = True
for m in matches:
    print(m, enabled)   
    if "don't" in m:
        enabled = False
    if m == "do()":
        enabled = True
    elif enabled:
        a, b = re.findall(r"\d+", m)
        p2 += int(a) * int(b)
    
    

print(p2)
    
    

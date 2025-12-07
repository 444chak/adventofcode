import os
from functools import lru_cache
import time
start_time = time.perf_counter()

# get path of the file
path = os.path.dirname(os.path.realpath(__file__))
FILE = os.path.join(path, "data.txt")
# Read data from file
with open(FILE, "r", encoding="utf-8") as f:
    data = [line.split(': ') for line in f.read().splitlines()]
    keys = [int(tot) for tot, _ in data]
    vals = [list(map(int, num.split(' '))) for _, num in data]


@lru_cache(None)
def addprod(L, start):
    if not L:
        return {start}
    if start is None:
        return addprod(tuple(L[1:]), L[0])
    return addprod(tuple(L[1:]), start * L[0]) | addprod(tuple(L[1:]), start + L[0])

@lru_cache(None)
def addprodconcat(L, start):
    if not L:
        return {start}
    if start is None:
        return addprodconcat(tuple(L[1:]), L[0])
    return addprodconcat(tuple(L[1:]), start * L[0]) | addprodconcat(tuple(L[1:]), start + L[0]) | addprodconcat(tuple(L[1:]), int(str(start) + str(L[0])))

P1 = 0
P2 = 0
n = len(keys)

for i in range(n):
    S = addprod(tuple(vals[i]), None)
    S2 = addprodconcat(tuple(vals[i]), None)
    if keys[i] in S:
        P1 += keys[i]
    if keys[i] in S2:
        P2 += keys[i]

print('Part 1 :', P1)
print('Part 2 :', P2)
print('Time taken:', time.perf_counter() - start_time)

import os
import time
import functools

start = time.time()
path = os.path.dirname(os.path.realpath(__file__))
file = path + "/data.txt"
with open(file, encoding="utf-8") as f:
    data = []
    data = f.read().splitlines()


available = data[0].split(", ")
requests = data[2:]


@functools.cache
def is_possible(c):
    if c == "":
        return True
    for a in available:
        if c.startswith(a) and is_possible(c[len(a) :]):
            return True
    return False


@functools.cache
def is_possible2(c):
    if c == "":
        return 1
    count = 0
    for a in available:
        if len(a) <= len(c) and c.startswith(a):
            count += is_possible2(c[len(a) :])
    return count


p1 = 0
p2 = 0
for request in requests:
    p1 += is_possible(request)
    p2 += is_possible2(request)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
print("Time taken: " + str(round(time.time() - start, 3)) + "s")

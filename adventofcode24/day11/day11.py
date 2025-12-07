import os
import time
from collections.abc import Iterable

# from adventofcode24.aoc_utils import aoc_utils

# aoc_utils.get_data()

path = os.path.dirname(os.path.realpath(__file__))
file = path + "/data.txt"
with open(file, encoding="utf-8") as f:
    data = []
    data = f.read().splitlines()

stones = [int(x) for x in data[0].split(" ")]
# ZERO, EVEN_NUMS = lambda x: x == 0, lambda x: len(x) % 2 == 0
# rules = {
#     ZERO: lambda x: 1,
#     EVEN_NUMS: lambda x:


print(stones)


def split_stone(stone):
    return int(str(stone)[: len(str(stone)) // 2]), int(
        str(stone)[len(str(stone)) // 2 :]
    )


def flatten(xs):
    for x in xs:
        if isinstance(x, Iterable) and not isinstance(x, str | bytes):
            yield from flatten(x)
        else:
            yield x


for _ in range(25):
    for i in range(len(stones)):
        if stones[i] == 0:
            stones[i] = 1
        elif len(str(stones[i])) % 2 == 0:
            stones[i] = [split_stone(stones[i])]
        else:
            stones[i] = stones[i] * 2024
    stones = list(flatten(stones))

print(len(stones))


def iterate(stones):
    cache = {}
    for stone in stones:
        cache[stone] = cache.get(stone, 0) + 1

    for _ in range(75):
        ncached = {}
        for k, v in cache.items():
            if k == 0:
                ncached[1] = ncached.get(1, 0) + v
            elif len(str(k)) % 2 == 0:
                a, b = split_stone(k)
                ncached[a] = ncached.get(a, 0) + v
                ncached[b] = ncached.get(b, 0) + v
            else:
                ncached[k * 2024] = ncached.get(k * 2024, 0) + v

        cache = ncached

    return sum(cache.values())


start = time.time()

print(iterate([int(x) for x in data[0].split(" ")]))
print(f"Time: {time.time() - start}")

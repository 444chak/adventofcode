"""
Advent of code 2025 - Day 3 - Part 1 & 2
https://adventofcode.com/2025/day/3
"""

import os
import sys

# Add the root directory to the path so we can import aoc_utils
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, root_dir)

from aoc_utils.aoc_utils import Timer, get_data  # noqa: E402

data = [list(map(int, line)) for line in get_data()]
timer = Timer()


# make the largest 2-digit number (but keep the order of the digits)
# 987654321111111 = 98
# 811111111111119 = 89
# 234234234234278 = 78
# 818181911112111 = 92

# [[9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1], = 98
# [8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], = 89
# [2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 7, 8], = 78
# [8, 1, 8, 1, 8, 1, 9, 1, 1, 1, 1, 2, 1, 1, 1], = 92


def largest_2_digit_number(list_of_numbers: list[int]) -> int:
    maxLeft = max(list_of_numbers[:-1])
    startIndex = list_of_numbers.index(maxLeft)
    maxRight = max(list_of_numbers[startIndex + 1 :])
    return maxLeft * 10 + maxRight


part1 = 0
for row in data:
    part1 += largest_2_digit_number(row)

print(part1)

# Part 2

# Same but with 12 digits (omg)

NUM_DIGITS_PART2 = 12


def largest_12_digit_number(list_of_numbers: list[int]) -> int:
    result = 0
    start_index = 0

    if len(list_of_numbers) < NUM_DIGITS_PART2:
        return 0

    for digit_position in range(NUM_DIGITS_PART2):
        remaining_digits = NUM_DIGITS_PART2 - digit_position - 1
        end_index = len(list_of_numbers) - remaining_digits
        max_value = max(list_of_numbers[start_index:end_index])
        slice_start = list_of_numbers[start_index:end_index]
        max_index = start_index + slice_start.index(max_value)

        result = result * 10 + max_value
        start_index = max_index + 1

    return result


part2 = 0
for row in data:
    part2 += largest_12_digit_number(row)

print(part2)

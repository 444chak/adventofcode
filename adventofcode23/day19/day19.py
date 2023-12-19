# pylint: disable=W0123
"""
Advent of code 2023 - Day 19 - Part 1 & 2
https://adventofcode.com/2023/day/19
"""

import os
import time
import operator
import re
from math import prod
path = os.path.dirname(os.path.realpath(__file__))
FILE = path + "/data.txt"

parts = []

workflows = {}

workflows["A"] = "acc"
workflows["R"] = "rej"

with open(FILE, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line.startswith("{"):
            parts.append(line[1:-1].split(","))
        elif line != "":
            workflows[line.split('{')[0]] = line.split('{')[1][:-1]

parts = [{vals.split("=")[0] : int(vals.split("=")[1]) for vals in part} for part in parts]

ops = {
    "<" : operator.lt,
    ">" : operator.gt,
    "True": lambda x, y: True,
}

def workflow(wf, p: dict):
    """
    Follow the workflow wf and return True if the part is accepted, False otherwise
    
    Args:
        wf (str): workflow to follow
        p (dict): values to check
        
    Returns:
        bool: True if accepted, False otherwise"""
    if wf == "acc":
        return True
    if wf == "rej":
        return False
    for i in wf.split(","):
        if ":" not in i:
            c, a = "True", i
        else:
            c, a = i.split(":")
            c = re.findall(r"([a-z])([<|>])(\d+)", c)[0]
        if c == "True":
            return workflow(workflows[a], p)
        elif ops[c[1]](p[c[0]], int(c[2])):
            return workflow(workflows[a], p)

time1 = time.time()
p1 = sum(sum(part.values()) for part in parts if workflow(workflows["in"], part))

print(f"Part 1 : {p1} in {time.time() - time1:.4f} seconds")


def range_split(r :range, n: int, op: str):
    """
    Split a range into two ranges.
    One containing the agreement values with operator op.
    The other containing the disagreement values

    Args:
        r (range): range to split
        n (int): value to compare
        op (str): operator to use

    Returns:
        tuple: tuple containing the two ranges (range_in, range_out)
    """
    if op == "<":
        range_in = range(r.start, n-1)
        range_out = range(n, r.stop)
    elif op == ">":
        range_in = range(n+1, r.stop)
        range_out = range(r.start, n)

    return range_in, range_out


ranges_accepted = []
def range_workflow(wf, p: dict):
    """
    Add to ranges_accepted the ranges that are accepted by the workflow
    
    Args:
        wf (str): workflow to follow
        p (dict): values to check
    """
    if wf == "acc":
        ranges_accepted.append(p)
        return True
    if wf == "rej":
        return False
    wf = wf.split(",")
    for seq in wf:
        if ":" not in seq:
            seq = "1:" + seq
        cond, goto = seq.split(":")
        if len(cond) != 1:
            cond = re.findall(r"([a-z])([<|>])(\d+)", cond)[0]
            cond = (cond[0], cond[1], int(cond[2]))
            rin, rout = range_split(p[cond[0]], cond[2], cond[1])
            pin = p.copy()
            pin[cond[0]] = rin
            p[cond[0]] = rout
            if len(rin) != 0:
                range_workflow(workflows[goto], pin)
        else:
            return range_workflow(workflows[goto], p)


time2 = time.time()
range_workflow(workflows["in"], {i:range(1,4000) for i in "xmas"})

P2 = 0
for acc_range in ranges_accepted:
    P2 += prod([v.stop - v.start + 1 for v in acc_range.values()])

print(f"Part 2 : {P2} in {time.time() - time2:.4f} seconds")

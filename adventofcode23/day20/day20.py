# pylint: disable=W0123
"""
Advent of code 2023 - Day 20 - Part 1 & 2
https://adventofcode.com/2023/day/20
"""

import os
from math import prod
import time
path = os.path.dirname(os.path.realpath(__file__))
FILE = path + "/data.txt"

t = time.time()

with open(FILE, "r", encoding="utf-8") as f:
    data = f.read().splitlines()


modules = {}
conj = {}
for line in data:
    mod, to = line.split(" -> ")
    if mod == 'broadcaster':
        modules['broadcaster'] = {'type': 'broadcaster', 'to': to.split(", ")}
    elif mod.startswith('%'):
        modules[mod[1:]] = {'type': '%', 'to': to.split(", "), 'state': 0}
    elif mod.startswith('&'):
        modules[mod[1:]] = {'type': '&', 'to': to.split(", ")}
    for c in to.split(", "):
        if c not in conj:
            conj[c] = {}
        conj[c][mod[1:]] = 0


pulses = {0: 0, 1: 0}

rx_pre = {i: 0 for i in conj[list(conj['rx'].keys())[0]]}

PRESSES = 0

while True:
    if PRESSES == 1000:
        print(f"Part 1: {prod(pulses.values())} in { time.time() - t:.4f} seconds")
    if all(rx_pre.values()):
        print(f"Part 2: {prod(rx_pre.values())} in { time.time() - t:.4f} seconds")
        break
    to_process = [['button', 'broadcaster', 0]]
    pulses[0] += 1
    log = []
    while to_process:
        source, mod, value = to_process.pop(0)
        log.append([mod, value])
        if mod not in modules:
            continue
        elif modules[mod]['type'] == 'broadcaster':
            for m in modules[mod]['to']:
                to_process.append([mod, m, value])
                pulses[value] += 1
        elif modules[mod]['type'] == '%':
            if value == 0:
                if modules[mod]['state'] == 1:
                    modules[mod]['state'] = 0
                else:
                    modules[mod]['state'] = 1
                for m in modules[mod]['to']:
                    to_process.append([mod, m, modules[mod]['state']])
                    pulses[modules[mod]['state']] += 1

        elif modules[mod]['type'] == '&':
            if 'rx' in modules[mod]['to']:
                for k,v in conj[mod].items():
                    if v == 1:
                        rx_pre[k] = PRESSES+1
            conj[mod][source] = value
            if all(conj[mod].values()):
                for m in modules[mod]['to']:
                    to_process.append([mod, m, 0])
                    pulses[0] += 1
            else:
                for m in modules[mod]['to']:
                    to_process.append([mod, m, 1])
                    pulses[1] += 1
    PRESSES += 1

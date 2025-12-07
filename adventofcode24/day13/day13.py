import os
import time

start = time.time()

path = os.path.dirname(os.path.realpath(__file__))
file = path + "/data.txt"
with open(file, encoding="utf-8") as f:
    data = []
    data = f.read().splitlines()

# print(data)

A_price = 3
B_price = 1

machines = []
machine = {}
for i, line in enumerate(data):
    if line == "":
        machines.append(machine)
        machine = {}
    else:
        l, r = line.split(":")
        l = l.split(" ")[-1]
        r = r.replace("X+", "")
        r = r.replace("Y+", "")
        r = r.replace("X=", "")
        r = r.replace("Y=", "")
        r = r.split(", ")
        r = list(map(int, r))
        machine[l] = r

machines.append(machine)


def ppcm(a, b):
    """
    Least common multiple
    """
    p = a * b
    while b:
        a, b = b, a % b
    return p // a


def solve_machine(machine, part2=False):
    """
    Go to Prize coordinate with the lowest cost and return token cost
    """
    PRICE = machine["Prize"]  # Prize coordinates (X, Y)
    if part2:
        PRICE[0] += 10000000000000
        PRICE[1] += 10000000000000
    A = machine["A"]  # A coordinates (+X, +Y)
    B = machine["B"]  # B coordinates (+X, +Y)

    # Find how many steps needed for each direction
    steps_A_x = PRICE[0] // A[0] if A[0] != 0 else float("inf")
    steps_A_y = PRICE[1] // A[1] if A[1] != 0 else float("inf")
    steps_B_x = PRICE[0] // B[0] if B[0] != 0 else float("inf")
    steps_B_y = PRICE[1] // B[1] if B[1] != 0 else float("inf")

    min_cost = float("inf")

    # Try different combinations of A and B moves
    for a_steps in range(max(steps_A_x, steps_A_y) + 2):
        for b_steps in range(max(steps_B_x, steps_B_y) + 2):
            pos_x = a_steps * A[0] + b_steps * B[0]
            pos_y = a_steps * A[1] + b_steps * B[1]

            if pos_x == PRICE[0] and pos_y == PRICE[1]:
                cost = a_steps * A_price + b_steps * B_price
                min_cost = min(min_cost, cost)

    return min_cost if min_cost != float("inf") else 0


def resoudre_equation(a1, b1, c1, a2, b2, c2):
    """
    Solve system of equations:
    a1*x + b1*y = c1
    a2*x + b2*y = c2
    Returns: x, y
    """
    y = (c2 * a1 - c1 * a2) / (a1 * b2 - a2 * b1)
    x = (c1 - b1 * y) / a1
    return x, y


p1 = 0
p2 = 0
for i, machine in enumerate(machines):
    x, y = resoudre_equation(
        machine["A"][0],
        machine["B"][0],
        machine["Prize"][0],
        machine["A"][1],
        machine["B"][1],
        machine["Prize"][1],
    )
    x_p2, y_p2 = resoudre_equation(
        machine["A"][0],
        machine["B"][0],
        machine["Prize"][0] + 10000000000000,
        machine["A"][1],
        machine["B"][1],
        machine["Prize"][1] + 10000000000000,
    )
    if int(x) == x and int(y) == y:
        p1 += 3 * x + y
    if int(x_p2) == x_p2 and int(y_p2) == y_p2:
        p2 += 3 * x_p2 + y_p2

print(f"Part 1: {int(p1)}")
print(f"Part 2: {int(p2)}")

print(f"Time: {time.time() - start}")

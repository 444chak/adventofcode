import os
import re
import time
from math import prod

start = time.time()

"""
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

path = os.path.dirname(os.path.realpath(__file__))
file = path + "/data.txt"
with open(file, encoding="utf-8") as f:
    data = []
    data = f.read().splitlines()


robots = [[int(x) for x in re.findall(r"-?\d+", line)] for line in data]

LARG = 101
LONG = 103
# LARG = 11
# LONG = 7

# crossing walls -> teleport at the other side of the wall


def deplacement(pos, vel):
    pos[0] = (pos[0] + vel[0]) % LARG
    pos[1] = (pos[1] + vel[1]) % LONG
    return pos


def print_grid(robots):
    output = ""
    for i in range(LONG):
        for j in range(LARG):
            if (j, i) in [tuple(x[:2]) for x in robots]:
                output += str([tuple(x[:2]) for x in robots].count((j, i)))
                # print(str([tuple(x[:2]) for x in robots].count((j, i))), end="")
            else:
                output += "."
                # print(".", end="")
        output += "\n"
        # print("")
    return output


from PIL import Image, ImageDraw


def write_image(robots, filename):
    """write the grid in a file"""
    with open(filename, "wb") as f:
        img = Image.new("RGB", (LARG, LONG), color="black")
        draw = ImageDraw.Draw(img)
        for robot in robots:
            draw.point(robot[:2], fill="white")
        img.save("adventofcode24/day14/" + filename, "PNG")


with open("output.txt", "w") as f:
    for i in range(10000):
        for robot in robots:
            robot[:2] = deplacement(robot[:2], robot[2:])
            # if i % 5 == 0:  # print every 5 iterations
        write_image(robots, "image" + str(i) + ".png")


def solve(robots):
    """count the number of robots in each quadrant"""
    count = [0, 0, 0, 0]
    HORIZONTAL_LINE = LONG // 2
    VERTICAL_LINE = LARG // 2
    for robot in robots:
        if robot[0] < VERTICAL_LINE and robot[1] < HORIZONTAL_LINE:
            count[0] += 1
        elif robot[0] < VERTICAL_LINE and robot[1] > HORIZONTAL_LINE:
            count[1] += 1
        elif robot[0] > VERTICAL_LINE and robot[1] < HORIZONTAL_LINE:
            count[2] += 1
        elif robot[0] > VERTICAL_LINE and robot[1] > HORIZONTAL_LINE:
            count[3] += 1
    return prod(count)


print(solve(robots))

print("Execution time: ", round(time.time() - start, 5))

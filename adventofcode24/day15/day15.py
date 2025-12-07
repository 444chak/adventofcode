import os
import re
import time

start = time.time()
path = os.path.dirname(os.path.realpath(__file__))
file = path + "/data.txt"
with open(file, encoding="utf-8") as f:
    data = []
    data = f.read().splitlines()

i = 0
for line in data:
    i += 1

    if line == "":
        break


def flatten(l):
    return [item for sublist in l for item in sublist]


movs = flatten([re.findall(r"[<^>v]", line) for line in data[i:]])

boxes = {
    (i, j) for i, line in enumerate(data) for j, char in enumerate(line) if char == "O"
}
walls = {
    (i, j) for i, line in enumerate(data) for j, char in enumerate(line) if char == "#"
}
robot = [
    (i, j) for i, line in enumerate(data) for j, char in enumerate(line) if char == "@"
]

move_dict = {"<": (0, -1), "^": (-1, 0), "v": (1, 0), ">": (0, 1)}


movs = [move_dict[move] for move in movs]


robot = robot[0]


for mov in movs:
    target = (robot[0] + mov[0], robot[1] + mov[1])
    if target not in walls and target not in boxes:
        robot = target
    else:
        target2 = target
        while target2 in boxes:
            target2 = (target2[0] + mov[0], target2[1] + mov[1])
        if target2 in walls:
            continue
        else:
            robot = target
            boxes.remove(target)
            boxes.add(target2)


p1 = sum(100 * i + j for i, j in boxes)
print(p1)

# Part 2

with open(file, encoding="utf-8") as f:
    data = []
    for line in f:
        data.append(
            line.replace("#", "##")
            .replace("O", "[]")
            .replace(".", "..")
            .replace("@", "@.")
            .strip()
        )


boxes = {
    (i, j) for i, line in enumerate(data) for j, char in enumerate(line) if char == "["
}

robot = [
    (i, j) for i, line in enumerate(data) for j, char in enumerate(line) if char == "@"
]

walls = {
    (i, j) for i, line in enumerate(data) for j, char in enumerate(line) if char == "#"
}

robot = robot[0]


def inter(target, boxes):
    return (
        target
        if target in boxes
        else (target[0], target[1] - 1)
        if (target[0], target[1] - 1) in boxes
        else tuple()
    )


def try_move(robot, mov, boxes):
    target = (robot[0] + mov[0], robot[1] + mov[1])
    if target in walls:
        return False, set()

    next_box = inter(target, boxes)
    if not next_box:
        return True, set()

    move_directions = {
        (0, -1): lambda pos: try_move(pos, mov, boxes),
        (0, 1): lambda pos: try_move((pos[0], pos[1] + 1), mov, boxes),
    }

    if mov in move_directions:
        can_move, moved_boxes = move_directions[mov](next_box)
        return can_move, moved_boxes | {next_box}

    can_move1, moved_boxes1 = try_move(next_box, mov, boxes)
    can_move2, moved_boxes2 = try_move((next_box[0], next_box[1] + 1), mov, boxes)
    return can_move1 and can_move2, moved_boxes1 | moved_boxes2 | {next_box}


for move in movs:
    move_bool, move_boxes = try_move(robot, move, boxes)
    if move_bool:
        boxes = {box for box in boxes if box not in move_boxes} | {
            (box[0] + move[0], box[1] + move[1]) for box in move_boxes
        }
        robot = (robot[0] + move[0], robot[1] + move[1])


p2 = sum(100 * i + j for i, j in boxes)

print(p2)  # 1472235


print("Time taken: " + str(round(time.time() - start, 3)) + "s")

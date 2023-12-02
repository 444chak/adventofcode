# 12 cubes rouges, 13 cubes verts et 14 cubes bleus
import re
with open('data.txt', 'r', encoding='utf-8') as f:
    data = f.read().split('\n')

# Part 1

"""
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

"""

for i in range(len(data)):

    data[i] = data[i].split(';')

for i in range(len(data)):
    for j in range(len(data[i])):
        
        data[i][j] = data[i][j].split(',')

# delete "Game x: " from each list
for i in range(len(data)):
    for j in range(len(data[i])):
        for k in range(len(data[i][j])):
            data[i][j][k] = data[i][j][k].replace('Game ' + str(i+1) + ': ', '')

theory = {
    'red': 12,
    'green': 13,
    'blue': 14
}
result = 0
for i in range(len(data)):
    possible = True
    for j in range(len(data[i])):
        for k in range(len(data[i][j])):
            for key, val in theory.items():
                if key in data[i][j][k]:
                    # get number of cubes in data (parse int)
                    number = re.findall(r'\d+', data[i][j][k])
                    if int(number[0]) > val:
                        possible = False

    if possible:
        result += i+1



# Part 2
powerall = 0
for i in range(len(data)):
    power = 0
    mini = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for j in range(len(data[i])):
        for k in range(len(data[i][j])):
            for key, val in mini.items():
                if key in data[i][j][k]:
                    number = re.findall(r'\d+', data[i][j][k])
                    if int(number[0]) > val:
                        mini[key] = int(number[0])
    power = mini['red'] * mini['green'] * mini['blue']
    powerall += power

print(powerall)
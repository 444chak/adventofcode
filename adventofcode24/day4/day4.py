import os

# get path of the file
path = os.path.dirname(os.path.realpath(__file__))
FILE = path + "/data.txt"

with open(FILE, "r", encoding="utf-8") as f:
    data = f.read().splitlines()

# Part 1 search "XMAS" -> horizontal, vertical, diagonalimport os

# get path of the file
path = os.path.dirname(os.path.realpath(__file__))
FILE = path + "/data.txt"

with open(FILE, "r", encoding="utf-8") as f:
    data = f.read().splitlines()

# Part 1 search "XMAS" -> horizontal, vertical, diagonal
def search_horizontal(data, word):
    count = 0
    for line in data:
        start = 0
        while start < len(line):
            pos = line.find(word, start)
            if pos == -1:
                break
            count += 1
            start = pos + 1
    return count

def search_vertical(data, word):
    count = 0
    for i in range(len(data[0])):
        col = ""
        for j in range(len(data)):
            col += data[j][i]
        start = 0
        while start < len(col):
            pos = col.find(word, start)
            if pos == -1:
                break
            count += 1
            start = pos + 1
    return count

def search_diagonal(data, word):
    count = 0
    rows = len(data)
    cols = len(data[0])
    
    # Diagonals from top-left to bottom-right
    for d in range(rows + cols - 1):
        diag = ""
        for i in range(max(0, d - cols + 1), min(rows, d + 1)):
            diag += data[i][d - i]
        start = 0
        while start < len(diag):
            pos = diag.find(word, start)
            if pos == -1:
                break
            count += 1
            start = pos + 1

    # Diagonals from bottom-left to top-right
    for d in range(rows + cols - 1):
        diag = ""
        for i in range(max(0, d - cols + 1), min(rows, d + 1)):
            diag += data[rows - 1 - i][d - i]
        start = 0
        while start < len(diag):
            pos = diag.find(word, start)
            if pos == -1:
                break
            count += 1
            start = pos + 1

    return count


def search(data, word):
    return search_horizontal(data, word) + search_horizontal(data, word[::-1]) + search_vertical(data, word) + search_vertical(data, word[::-1]) + search_diagonal(data, word) + search_diagonal(data, word[::-1])

print(search(data, "XMAS"))

# Part 2

# search "MAS" cross
count = 0
for i in range(1, len(data) - 1):
    for j in range(1, len(data[0]) - 1):
        if data[i][j] == "A":
            if ((data[i-1][j-1] == "M" and data[i+1][j+1] == "S") or (data[i-1][j-1] == "S" and data[i+1][j+1] == "M")) and \
               ((data[i-1][j+1] == "M" and data[i+1][j-1] == "S") or (data[i-1][j+1] == "S" and data[i+1][j-1] == "M")):
                count += 1

print(count)

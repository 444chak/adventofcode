import os

# get path of the file 
path = os.path.dirname(os.path.realpath(__file__))
FILE = path + "/data.txt"
def part1():
    with open(FILE) as f:
        sum = 0
        for i in f.readlines():
            nb = []
            for j in i:
                if j.isdigit():
                    # concatenate the digits
                    nb.append(j)

            nb = nb[0] + nb[-1]
            sum += int(nb)

    print(sum)

    
part1()


# bonus
print(sum(int(nb[0] + nb[-1]) for nb in [list(filter(str.isdigit, i)) for i in open(FILE)]))


numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
}

def part2():
    with open(FILE) as f:
        sum = 0
        for i in f.readlines():
            nb = []
            string = ""
            for j in i:
                if j.isalpha():
                    string += j
                    for k in numbers:
                        if k in string:
                            nb.append(numbers[k])
                            string = string[-1] # most important line
                if j.isdigit():
                    nb.append(j)

            nb = str(nb[0]) + str(nb[-1])
            sum += int(nb)

    print(sum)

part2()


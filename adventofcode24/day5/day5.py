import os

# get path of the file
path = os.path.dirname(os.path.realpath(__file__))
FILE = path + "/data.txt"

rules = {}

updates = []

with open(FILE, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            break
        rule, next = line.split("|")
        if rules.get(int(rule)) is None:
            rules[int(rule)] = []
        rules[int(rule)].append(int(next))
    for line in f:
        updates.append([int(x) for x in line.split(",")])


updates_ok = []
updates_not_ok = []
        
for update in updates:
    ok = True
    no_ok_factor = None
    for i in range(len(update)):
        for c in update[i + 1:]:
            if c in rules.keys():
                if update[i] in rules[c]:
                    ok = False
                    no_ok_factor = c
                    break
    if ok:
        updates_ok.append(update)
    else:
        updates_not_ok.append((update, no_ok_factor))


p1 = 0

for update in updates_ok:
    p1 += update[len(update) // 2]

print(p1)


# Part 2

news = []

for update, no_ok_factor in updates_not_ok:
    new = []
    for c in update:
        for oc in new:
           if oc in rules.keys() and c in rules[oc]:
                new.insert(new.index(oc), c)
                break
        else:
            new.append(c)
    news.append(new)


p2 = 0
for update in news:
    # print(update[len(update) // 2])
    p2 += update[len(update) // 2]

print(p2)
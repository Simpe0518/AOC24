file = open("d8.txt", "r")
inst = []
nodes = {}
tot_p1 = 0
tot_p2 = 0

for line in file.readlines():
    inst.append(list(line.rstrip()))

SIZE = len(inst)

def in_range(v):
    if v < 0:
        return False
    elif v > SIZE-1:
        return False
    return True

for y in range(SIZE):
    for x in range(SIZE):
        if inst[y][x] != '.':
            if inst[y][x] in nodes.keys():
                nodes[inst[y][x]].append((y,x))
            else:
                nodes[inst[y][x]] = [(y,x)]

### part 1 ###

for x in nodes.keys():
    for i in nodes[x]:
        for j in nodes[x]:
            if i != j:
                pos1 = i[0] + i[0] - j[0]
                pos2 = i[1] + i[1] - j[1]
                if in_range(pos1) and in_range(pos2):
                    inst[pos1][pos2] = '#'

tot_p1 =+ sum([len([a for a in line if a == '#']) for line in inst])


print(tot_p1)



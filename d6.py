file = open("d6.txt", "r")
inst = []
off_sets = [(-1,0),(0,1),(1,0),(0,-1)]
in_bounds = True
direction = 0

for line in file.readlines():
    inst.append(list(line.rstrip()))

SIZE = len(inst)
print(SIZE)

pos = [[ix,iy] for ix, row in enumerate(inst) for iy, i in enumerate(row) if i == '^'][0]

### part 1 ###

while in_bounds:

    inst[pos[0]][pos[1]] = 'X'

    if inst[pos[0]+off_sets[direction % 4][0]][pos[1]+off_sets[direction % 4][1]] == '#':
        direction = direction + 1

    pos[0] = pos[0] + off_sets[direction % 4][0]
    pos[1] = pos[1] + off_sets[direction % 4][1]

    if pos[0] > SIZE or pos[1] > SIZE or pos[0] < 0 or pos[1] < 0:
        print(pos)
        in_bounds = False
    
for x in inst:     
        print(*x, sep='')

print(sum(x.count('X') for x in inst))
print(direction / 4)

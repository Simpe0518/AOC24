file = open("d10.txt", "r")
inst = []
tot_p1 = 0
tot_p2 = 0

for line in file.readlines():
    inst.append(list(map(int, line.rstrip())))

SIZE = len(inst)

def in_range(v):
    if  v < 0 or  v > SIZE-1:
        return False
    return True

### part 1 ###
def find_peaks(y, x, elev):
    if elev == 9:
        return [(y,x)]

    b = set()
    
    for yi, xi in ((y+1, x),(y-1,x),(y,x+1),(y,x-1)):
        if in_range(yi) and in_range(xi) and inst[yi][xi] == elev + 1:
            b.update(find_peaks(yi,xi,elev+1))
    return b

### part 2 ###

def find_paths(y, x, elev):
    return sum([find_paths(yi, xi, elev+1) for yi, xi in ((y+1, x),(y-1,x),(y,x+1),(y,x-1)) if in_range(yi) and in_range(xi) and inst[yi][xi] == elev+1]) if elev != 9 else 1


trailheads = [[ix,iy] for ix, row in enumerate(inst) for iy, i in enumerate(row) if i == 0]

for pos in trailheads:
    tot_p1 += len(find_peaks(pos[0], pos[1], 0))
    tot_p2 += find_paths(pos[0], pos[1], 0)

print(tot_p1)
print(tot_p2)


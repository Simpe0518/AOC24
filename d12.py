file = open("d12.txt", "r")
inst = []
plot_fence = {}
plot_area = {}
id = 0

tot_p1 = 0
tot_p2 = 0

for line in file.readlines():
    inst.append(list(line.rstrip()))

SIZE = len(inst)
value_map = [[0 for i in range(SIZE)] for j in range(SIZE)]

def in_range(v):
    if  v < 0 or  v > SIZE-1:
        return False
    return True

def fill_zone(y,x,plot,id):
    if inst[y][x] == plot:
        value_map[y][x] = id
        for yi, xi in ((y+1, x),(y-1,x),(y,x+1),(y,x-1)):
            if in_range(yi) and in_range(xi) and inst[yi][xi] == plot and value_map[yi][xi] == 0:
                fill_zone(yi,xi,plot,id)


for y in range(SIZE):
    for x in range(SIZE):
        if value_map[y][x] == 0:
            id += 1
            fill_zone(y,x,inst[y][x], id)


for y in range(SIZE):
    for x in range(SIZE):
        outside_neighbors = 0
        for yi, xi in ((y+1, x),(y-1,x),(y,x+1),(y,x-1)):
            if not in_range(yi) or not in_range(xi) or value_map[y][x] != value_map[yi][xi]:
                outside_neighbors += 1
        if value_map[y][x] in plot_fence.keys():
            plot_fence[value_map[y][x]] += outside_neighbors
        else:
            plot_fence[value_map[y][x]] = outside_neighbors
        if value_map[y][x] in plot_area.keys():
            plot_area[value_map[y][x]] += 1
        else:
            plot_area[value_map[y][x]] = 1

for plot in plot_area.keys():
    tot_p1 += plot_area[plot] * plot_fence[plot]

print(tot_p1)
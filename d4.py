file = open("d4.txt", "r")
inst = []
MAS = "MAS"
MS = "MS"
tot_p1 = 0
tot_p2 = 0

for line in file.readlines():
    inst.append(list(line.rstrip()))

MAX = len(inst) 

### Part 1 ###

for x in range(MAX):
    for y in range(MAX):
        if inst[x][y] == 'X':
            if x < MAX - 3:
                if inst[x+1][y] + inst[x+2][y] + inst[x+3][y] == MAS:
                    tot_p1 = tot_p1 + 1
            if x >= 3:
                if inst[x-1][y] + inst[x-2][y] + inst[x-3][y] == MAS:
                    tot_p1 = tot_p1 + 1
            if y < MAX - 3:
                if inst[x][y+1] + inst[x][y+2] + inst[x][y+3] == MAS:
                    tot_p1 = tot_p1 + 1
            if y >= 3:
                if inst[x][y-1] + inst[x][y-2] + inst[x][y-3] == MAS:
                    tot_p1 = tot_p1 + 1
            if y < MAX - 3 and x < MAX - 3:  
                if inst[x+1][y+1] + inst[x+2][y+2] + inst[x+3][y+3] == MAS:
                    tot_p1 = tot_p1 + 1
            if  y >= 3 and x >= 3:
                if inst[x-1][y-1] + inst[x-2][y-2] + inst[x-3][y-3] == MAS:
                    tot_p1 = tot_p1 + 1
            if x < MAX - 3 and y >= 3:
                if inst[x+1][y-1] + inst[x+2][y-2] + inst[x+3][y-3] == MAS:
                    tot_p1 = tot_p1 + 1
            if x >= 3 and y < MAX - 3:
                if inst[x-1][y+1] + inst[x-2][y+2] + inst[x-3][y+3] == MAS:
                    tot_p1 = tot_p1 + 1

### Part 2 ###

for x in range(1, MAX-1):
    for y in range(1, MAX-1):
        if inst[x][y] == 'A':
            if inst[x+1][y+1] + inst[x-1][y-1] in "MSM" and inst[x+1][y-1] + inst[x-1][y+1] in "MSM":
                tot_p2 = tot_p2 + 1

print(tot_p1)
print(tot_p2)


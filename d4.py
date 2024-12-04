
file = open("d4.txt", "r")
inst = []
XMAS = ['X','M','A','S']
MAS = "MAS"
tot_p1 = 0
x = []

for line in file.readlines():
    inst.append(list(line.rstrip()))


MAX = len(inst) 

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

print(tot_p1)

































"""
def find_xmas(x,y,n=0,tot=0):
    if x > X_MAX or y > Y_MAX or x < 0 or y < 0:
        return 0

    if inst[x][y] == XMAS[n]:
        n = n + 1

        if n == 1:
            for off_set in octile(1):
                tot = tot + find_xmas(x+off_set[0], y+off_set[1], n, tot)
        elif n < 3:
            tot = tot + find_xmas(x, y, n, tot)
        else:
            return tot + 1
    return tot
   

def octile(size):

    octiles = []

    for x in range(size*2):
        octiles.append([x-size+1, size])
        octiles.append([x-size, -size]) 
    for y in range(size*2):
        octiles.append([size, y-size]) 
        octiles.append([-size, y-size+1])

    return octiles


#print(octile(1))



for x in range(X_MAX):
    for y in range(Y_MAX):
             tot_p1 = tot_p1 + find_xmas(x, y)
             print(tot_p1)

print(tot_p1)

"""

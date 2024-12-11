file = open("d11.txt", "r")
inst = []
tot_p1 = 0
tot_p2 = 0

for line in file.readlines():
    inst = list(map(int, line.rstrip().split()))

for blink in range(25):
    i = 0
    while i < len(inst):
        if inst[i] == 0:
            inst[i] = 1
        elif len(str(inst[i])) % 2 == 0:
            front = int(''.join(list(str(inst[i]))[:(len(str(inst[i]))//2)]))
            back = int(''.join(list(str(inst[i]))[(len(str(inst[i]))//2):]))
            inst.insert(i, front)
            inst[i+1] = back
            i+=1
        else:
            inst[i] *= 2024
        i+=1
        

tot_p1 = len(inst)

print(tot_p1)


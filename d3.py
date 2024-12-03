import re
import math

file = open("d3.txt", "r")
inst = []
tot_p1 = 0
tot_p2 = 0
do = True

for line in file.readlines():
    inst.append(line)

### part 1 ###

for line in inst:
    seqs = re.findall("mul\((\d+,\d+)\)",line)
    for seq in seqs:
        tot_p1 = tot_p1 + math.prod(list(map(int,seq.split(","))))


### part 2 ###

for line in inst:
    seqs = re.findall("mul\((\d+,\d+)\)+|(do\(\))+|(don't\(\))+",line)
    for seq in seqs:
        seq = list(filter(None, seq))[0]
        if seq == "do()":
            do = True
        elif seq == "don't()":
            do = False
        elif do:
            tot_p2 = tot_p2 + math.prod(list(map(int,seq.split(","))))

print(tot_p1)
print(tot_p2)

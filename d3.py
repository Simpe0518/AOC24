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
    x = re.findall("mul\((\d+,\d+)\)",line)
    for pair in x:
        tot_p1 = tot_p1 + math.prod(list(map(int,pair.split(","))))


### part 2 ###

for line in inst:
    x = re.findall("mul\((\d+,\d+)\)+|(do\(\))+|(don't\(\))+",line)
    for pair in x:
        pair = list(filter(None, pair))[0]
        if pair == "do()":
            do = True
        elif pair == "don't()":
            do = False
        elif do:
            tot_p2 = tot_p2 + math.prod(list(map(int,pair.split(","))))

print(tot_p1)
print(tot_p2)

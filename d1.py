file = open("d1.txt", "r")
left = []
right = []
tot_p1 = 0
tot_p2 = 0

for line in file.readlines():
    left.append(line.split()[0])
    right.append(line.split()[1])

left.sort()
right.sort()

### part 1 ###

for i in range(len(left)):
    tot_p1 = tot_p1 + (abs(int(left[i]) - int(right[i])))

print(tot_p1)

## part 2 ###

for i in range(len(left)):
    tot_p2 = tot_p2 + (int(left[i]) * right.count(left[i]))

print (tot_p2)
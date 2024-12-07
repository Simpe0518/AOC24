file = open("d7.txt", "r")
inst = []
tot = 0

for line in file.readlines():
    inst.append(list(map(int, line.replace(':', '').split())))

def valid(n, seq):
    if len(seq) == 1:
        return 1 if n == seq[0] else 0
    return n if valid(n,[seq[0]+seq[1]]+seq[2:]) + valid(n,[seq[0]*seq[1]]+seq[2:]) + valid(n,[int(str(seq[0])+str(seq[1]))]+seq[2:])> 0 else 0

### part 1 & 2 ###
for seq in inst:
    tot = tot + valid(seq[0], seq[1:])

print(tot)
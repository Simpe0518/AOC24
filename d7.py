file = open("d7.txt", "r")
inst = []
tot_p1 = 0
tot_p2 = 0

for line in file.readlines():
    inst.append(list(map(int, line.replace(':', '').split())))

def valid(n, seq, conc):
    if len(seq) == 1:
        return 1 if n == seq[0] else 0
    return n if valid(n,[seq[0]+seq[1]]+seq[2:],conc) + valid(n,[seq[0]*seq[1]]+seq[2:],conc) + (valid(n,[int(str(seq[0])+str(seq[1]))]+seq[2:],conc) if conc else 0)  > 0 else 0

### part 1 & 2 ###
for seq in inst:
    tot_p1 = tot_p1 + valid(seq[0], seq[1:], False)
    tot_p2 = tot_p2 + valid(seq[0], seq[1:], True)

print(tot_p1)
print(tot_p2)
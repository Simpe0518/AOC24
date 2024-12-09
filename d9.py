file = open("d9.txt", "r")
inst = []
id_list = []
id = 0
j = 0
tot_p1 = 0
tot_p2 = 0
even = True

inst = file.readlines()[0].strip()

for n in inst:
    even = not even
    for i in range(int(n)):
        if even:
            id_list.append('.')
        else:
            id_list.append(id)
    if not even:
        id += 1

### part 1 ### 

while  j < len(id_list):
    if id_list[j] == '.':
        back = '.'
        while back == '.':
            back = id_list.pop()
        id_list[j] = back
    j += 1

for i in range(len(id_list)):
    tot_p1 += i * id_list[i]

print(tot_p1)
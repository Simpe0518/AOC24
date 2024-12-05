file = open("d5.txt", "r")
rules_dict = {}
#rules_list = []
page_nrs = []
bad_page_nrs = []
pages = True
tot_p1 = 0
tot_p2 = 0

for line in file.readlines():
    if line == '\n':    #blank line
        pages = False
    elif pages:
        rule = list(map(int, line.rstrip().split('|')))
        #rules_list.append(rule)
        if rule[0] in rules_dict.keys():
            rules_dict[rule[0]].append(rule[1])
        else:
            rules_dict[rule[0]] = [rule[1]]
    else:
        page_nrs.append(list(map(int,line.rstrip().split(','))))

def is_valid(page):
    valid = True
    for i in range(1, len(page)):
        if page[i-1] in rules_dict.keys():
            for nr in page[i:]:
                if nr not in rules_dict[page[i-1]]:
                    valid = False
        else:
            valid = False
    return valid

### part 1 ###

for page in page_nrs:
    if is_valid(page):
        tot_p1 = tot_p1 + page[((len(page) - 1) // 2)]
    else:
        bad_page_nrs.append(page)

### part 2 ###

def page_sort(n):
    return 0

#print(page_nrs[1:2])
#print(rules_list)


for page in bad_page_nrs:
    sorted_list = sorted(page, key=lambda x: len([a for a in page if is_valid([x,a])]), reverse=True)
    tot_p2 = tot_p2 + sorted_list[((len(sorted_list) - 1) // 2)]

    


print(tot_p1)
print(tot_p2)


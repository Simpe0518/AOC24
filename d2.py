import copy
file = open("d2.txt", "r")

reports = []
safe_p1 = 0
safe_p2 = 0

for line in file.readlines():
    reports.append(list(map(int,line.split())))



def is_safe(report):
    for i in range(1, len(report)):
        diff = abs(report[i] - report[i-1])
        if  3 < diff or 1 > diff:
            return False
    
    if report != sorted(report) and report != sorted(report, reverse = True):
        print(report)
        return False
    return True

### part 1 ###
for report in reports:
    if is_safe(report):
        safe_p1 = safe_p1 + 1

### part 2 ###
    else:
        safe = False
        for i in range(len(report)):
            a = copy.copy(report)
            a.pop(i)
            if is_safe(a):
                safe = True
        if safe:
            safe_p2 = safe_p2 + 1



print(safe_p1)
print(safe_p1+safe_p2)





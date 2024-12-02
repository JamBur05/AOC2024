file = open("input.txt", "r")

list1 = []
totalSafe = 0
gradient = 0
diff = 0


for x in file:
    list1.append(x)

for x in list1:
    row = x.split(" ")
    for i in range(len(row) - 1):
        diff = int(row[i]) - int(row[i + 1])
        if diff == 0:
            break
        elif i == 0:
            if diff > 0:
                gradient = 1/diff * diff
            else:
                gradient = (1/diff * diff) * -1
        if abs(diff) > 3:
            break
        if (gradient > 0 and diff < 0) or (gradient < 0 and diff > 0):
            break

        if i == len(row) - 2:
           totalSafe += 1


print(totalSafe)

'''
Days              : 0
Hours             : 0
Minutes           : 0
Seconds           : 0
Milliseconds      : 49
Ticks             : 496072
TotalDays         : 5.74157407407407E-07
TotalHours        : 1.37797777777778E-05
TotalMinutes      : 0.000826786666666667
TotalSeconds      : 0.0496072
TotalMilliseconds : 49.6072
'''
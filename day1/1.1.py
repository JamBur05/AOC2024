file = open("input.txt", "r")

list1 = []
list2 = []
total = 0

for x in file:
    data = x.split("   ")
    list1.append(int(data[0]))
    list2.append(int(data[1]))

list1.sort()
list2.sort()

for i in range(len(list1)):
    total += abs(list1[i] - list2[i])

print(total)

'''
Days              : 0
Hours             : 0
Minutes           : 0
Seconds           : 0
Milliseconds      : 52
Ticks             : 525550
TotalDays         : 6.08275462962963E-07
TotalHours        : 1.45986111111111E-05
TotalMinutes      : 0.000875916666666667
TotalSeconds      : 0.052555
TotalMilliseconds : 52.555
'''
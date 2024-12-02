def CheckPairs(row):
    for i in range(len(row) - 1):
        diff = int(row[i]) - int(row[i + 1])
        if diff == 0:
            return False
        elif i == 0:
            if diff > 0:
                gradient = 1/diff * diff
            else:
                gradient = (1/diff * diff) * -1
        if abs(diff) > 3:
            return False
        if (gradient > 0 and diff < 0) or (gradient < 0 and diff > 0):
            return False
    
    return True

def Dampener(row):
    if CheckPairs(row):
        return True
    
    for i in range(len(row)):
        modifiedRow = row[:i] + row[i + 1:]
        if CheckPairs(modifiedRow):
            return True
    
    return False

file = open("input.txt", "r")

list1 = []
totalSafe = 0

for x in file:
    list1.append(x)

for x in list1:
    row = x.split(" ")
    if Dampener(row):
        totalSafe += 1

print(totalSafe)

'''
Days              : 0
Hours             : 0
Minutes           : 0
Seconds           : 0
Milliseconds      : 49
Ticks             : 490923
TotalDays         : 5.68197916666667E-07
TotalHours        : 1.363675E-05
TotalMinutes      : 0.000818205
TotalSeconds      : 0.0490923
TotalMilliseconds : 49.0923
'''
def CheckPairs(row):
    gradient = int(row[1]) - int(row[0])
    for i in range(1, len(row) - 1):
        diff = int(row[i + 1]) - int(row[i])
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        elif (gradient > 0 and diff < 0) or (gradient < 0 and diff > 0):
            return False
            
    return True


def SafeWithDampener(row):
    if CheckPairs(row):
        return True
    
    for i in range(1, len(row) - 1):
        modified_row = row[:i] + row[i + 1:]
        if CheckPairs(modified_row):
            return True
    
    return False


file = open("input.txt", "r")

list1 = []
totalSafe = 0

for x in file:
    list1.append(x)

for x in list1:
    row = x.split(" ")
    if SafeWithDampener(row):
        totalSafe += 1

print(totalSafe)
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

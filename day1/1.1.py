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
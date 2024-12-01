file = open("input.txt", "r")

list1 = []
list2 = []
total = 0

for x in file:
    data = x.split(" ")
    list1.append(data[0])
    list2.append(data[3])

list1.sort()
list2.sort()

for i in range(len(list1)):
    if list1[i] >= list2[i]:
        total += (int(list1[i]) - int(list2[i]))
    else:
        total += (int(list2[i]) - int(list1[i]))

print(total)
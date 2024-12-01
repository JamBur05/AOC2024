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
    counter = 0
    for j in range(len(list2)):
        if(int(list1[i]) == int(list2[j])):
            counter += 1
        
    total += int(list1[i]) * counter

print(total)
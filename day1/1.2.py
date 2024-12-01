import time
start_time = time.perf_counter()

file = open("input.txt", "r")

list1 = []
list2 = []
total = 0

for x in file:
    data = x.split("   ")
    list1.append(int(data[0]))
    list2.append(int(data[1]))

input_reading_time = (time.perf_counter() - start_time) * 1_000_000  # Convert to microseconds
print(f"Time for reading and processing input: {input_reading_time:.2f} microseconds")

start_time = time.perf_counter()

for i in range(len(list1)):
    counter = 0
    for j in range(len(list2)):
        if(list1[i] == list2[j]):
            counter += 1
        
    total += list1[i] * counter

computation_time = (time.perf_counter() - start_time) * 1_000_000  # Convert to microseconds
print(f"Time for computations: {computation_time:.2f} microseconds")

print(total)
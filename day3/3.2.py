import re

file = open("input.txt", "r")
regex = []
numbers = []
result = 0
score = 0
isDo = True


for x in file:
    regex += re.findall(r"mul\(\d+, *\d+\)|do\(\)|don't\(\)", x)

for x in regex:
    if "do()" in x:
        isDo = True
        continue
    
    if "don't()" in x:
        isDo = False
        continue

    if "mul" in x and isDo == True:
        xList = x.split(",")
        numbers = re.findall(r"\d+", x)
        result = int(numbers[0]) * int(numbers[1])
        score += result

print(score)

'''
Days              : 0
Hours             : 0
Minutes           : 0
Seconds           : 0
Milliseconds      : 65
Ticks             : 657645
TotalDays         : 7.61163194444444E-07
TotalHours        : 1.82679166666667E-05
TotalMinutes      : 0.001096075
TotalSeconds      : 0.0657645
TotalMilliseconds : 65.7645
'''
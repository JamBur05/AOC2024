import re

file = open("input.txt", "r")
regex = []
score = 0

for x in file:
    regex += re.findall(r"mul\(\d+, *\d+\)", x)

for x in regex:
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
Milliseconds      : 75
Ticks             : 753121
TotalDays         : 8.71667824074074E-07
TotalHours        : 2.09200277777778E-05
TotalMinutes      : 0.00125520166666667
TotalSeconds      : 0.0753121
TotalMilliseconds : 75.3121
'''
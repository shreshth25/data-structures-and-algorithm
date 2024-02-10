import math
s = [2, 5, 6, 10, 1, 3, 12, 4]

first_max = -math.inf
second_max = -math.inf

for i in s:
    if i>= first_max:
        second_max = first_max
        first_max = i
    elif i>second_max:
        second_max = i

print(second_max)
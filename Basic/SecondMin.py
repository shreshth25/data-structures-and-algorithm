import math
s = [2, 5, 6, 10, 1, 3, 12, 4]

first_min = math.inf
second_min = math.inf

for i in s:
    if i<= first_min:
        second_min = first_min
        first_min = i
    elif i<second_min:
        second_min = i

print(second_min)
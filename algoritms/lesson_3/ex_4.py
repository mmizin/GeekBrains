# Определить, какое число в массиве встречается чаще всего.

array = [1,2,3,4,5,6,3,4,5,3]
d = {}

for num in array:
    if num not in d:
        d[num] = 1
    else:
        d[num] += 1

max_count = sorted(d.values())[-1]
for key, val in d.items():
    if val == max_count:
        print(key)

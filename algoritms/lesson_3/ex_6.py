# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

l = [2, 1, 2, 3, 2, 9, 2]

tmp = list(l)
i = 0

while i < len(l) - 1:
    if tmp[i] > tmp[i + 1]:
        tmp[i], tmp[i+1] = tmp[i + 1], tmp[i]
        i = 0
    else:
        i += 1

min_n, max_n = tmp[0], tmp[-1]
idx_min = l.index(min_n)
idx_max = l.index(max_n)
res = 0

for num in l[idx_min+1:idx_max]:
    res += num

print(res)
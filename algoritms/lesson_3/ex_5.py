# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

l = [1, -1, 2, -2, 3, -3, 4, -4]
tmp = list(l)
i = 0

while i < len(l) - 1:
    if tmp[i] > tmp[i + 1]:
        tmp[i], tmp[i+1] = tmp[i + 1], tmp[i]
        i = 0
    else:
        i += 1

print(f'The biggest negative number is {tmp[0]}, it\'s position in array {l.index(tmp[0])}.')


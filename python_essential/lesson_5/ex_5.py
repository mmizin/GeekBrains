# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import sample

numbers = sample(range(100, 200), 10)

with open('ex_5.txt', 'w+') as f:
    f.write(' '.join(map(lambda x: str(x), numbers)))
    f.seek(0)
    print(sum(map(lambda num: int(num), f.read().split())))


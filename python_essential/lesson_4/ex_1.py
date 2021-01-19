#  Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
#  В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
#  Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

if len(argv) == 4:
    argv = list(map(lambda x: float(x), argv[1:]))
    salary = argv[0] * argv[1] + argv[2]
    print(f'Salary equals: ${salary}')
else:
    print(f'Not enough arguments. You should pass 3 arguments(work_time, rate_per_hour, bonus) and You have passed only '
          f'{len(argv) - 1} arguments')


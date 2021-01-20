# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import csv
import json
from functools import reduce

wages = 0
count = 1

with open('ex_7.csv') as csv_f:
    csv_reader = csv.reader(csv_f)

    data = [{v.split()[0]: reduce(lambda n, m: n - m, list(map(lambda x: int(x), v.split()[2:])))}
            for k in csv_reader for v in k]

for item in data:
    for key, val in item.items():
        if val < 0:
            item.update({key: 'losses_loom_larger_than_gains'})
        else:
            wages += val
            count += 1


data.append({'average_profit': wages / count })

with open('ex_7.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)


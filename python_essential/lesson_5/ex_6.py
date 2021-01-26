# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

import re

with open('ex_6.txt', 'r') as f:
    content = f.readlines()

lesson_name = [lesson.partition(':')[0] for lesson in content]
load = [sum(list(map(lambda x: int(x), re.findall(r'[-+]?\d*\.\d+|\d+', load))))
        for line in content for load in line.split(' -')]
result = dict(zip(lesson_name, load))
print(result)



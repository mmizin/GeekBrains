# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

import csv

SALARY_RATE = 20000
data_list = {'names': [],
             'average_salary': []}

with open('ex_3.csv') as csvfile:
    reader = csv.DictReader(csvfile, ['name', 'salary'])
    for item in reader:
        if int(item['salary']) < SALARY_RATE:
            data_list['names'].append(item['name'])
        data_list['average_salary'].append(int(item['salary']))

print(f'The {data_list["names"]} has/have salary lower than {SALARY_RATE}'
      f'\n The average salary of the staff is equal: {sum(data_list["average_salary"]) / len(data_list["average_salary"])}')



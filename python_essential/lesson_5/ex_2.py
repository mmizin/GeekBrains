# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('ex_2.txt', 'r') as reader:
    for index, value in enumerate(reader, 1):
        print(f'The line #{index} has {len(value.split())} words')

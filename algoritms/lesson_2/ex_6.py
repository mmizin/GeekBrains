# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел
# и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

num_sequence = input('Enter your number: ')
num_to_find = input('Enter number to find: ')
count = 0

for n in num_sequence:
    if n == num_to_find:
        count += 1

print(f'The "{num_to_find}" number was met in "{num_sequence}" {count} times')
# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

result_string = ''
num = 4


def infinite_sequence(num):
    count = 1
    factorial = 1
    while num:
        factorial *= count
        yield factorial
        count += 1
        num -= 1


for index, fact in enumerate(infinite_sequence(num), 1):
    if index == num:
        result_string += f'{index} = {fact}'
        break
    result_string += f'{index} * '

print(result_string)

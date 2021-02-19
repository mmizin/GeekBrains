# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
# если введено число 3486, надо вывести 6843.

def req(num):
    if num:
        print(num % 10, end='')
        req(num // 10)


input_num = int(input('Enter your number: '))

req(input_num)

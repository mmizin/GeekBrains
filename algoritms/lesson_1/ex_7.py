# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))

if a < b < c or c < b < a:
    print(f'The average from {a} {b} {c} : {b}')
elif b < a < c or c < a < b:
    print(f'The average from {a} {b} {c} : {a}')
else:
    print(f'The average from {a} {b} {c} : {c}')

# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = int(input('Enter your num: '))
even = []
odd = []

while num:
    if (num % 10) % 2 == 0:
        even.append(num % 10)
    else:
        odd.append(num % 10)

    num //= 10

print(f'We have {len(even)} even numbers: {even}')
print(f'We have {len(odd)} odd numbers: {odd}')

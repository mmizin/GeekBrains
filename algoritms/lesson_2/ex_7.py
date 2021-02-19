# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и
# сумму его цифр.

nums = list(map(lambda x: int(x), input('Enter your numbers, e.g. 123 789 478: ').split()))
res = {}


for num in nums:
    value = 0
    key = ''
    while num:
        key += ''.join(str(num % 10)) + '+'
        value += num % 10
        num //= 10

    key = key[:-1]
    res[key] = value

print(f'The biggest number is {res[max(res, key=res.get)]} by sum of {max(res, key=res.get)}')

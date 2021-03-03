import math

print('Enter please numbers for equation: ax^2 +bx +c = 0 ')

a = float(input('Enter please a: '))
b = float(input('Enter please b: '))
c = float(input('Enter please c: '))

discr = b ** 2 - 4 * a * c
print(discr)
print(f'D = {discr:.2f}')

if discr > 0:  # we will have 2 roots: x1,x2 = -b +/- math.sqrt(D) / 2a
    x1 = (-b - math.sqrt(discr)) / (2 * a)
    x2 = (-b + math.sqrt(discr)) / (2 * a)
    print(f'x1 = {x1:.2f} and x2 = {x2:.2f}')
elif discr == 0:  # x = -b / 2a
    x = -b / (2 * a)
    print(f'x = {x:.2f}')
else:
    print("The roots are not exist")


# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из
# этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным
# или равносторонним.

a = float(input('Enter the length of the first triangle side: '))
b = float(input('Enter the length of the second triangle side: '))
c = float(input('Enter the length of the third triangle side: '))

if a == b and b == c:
    print('Equilateral triangle')
elif a != b and a != c and b != c:
    print('Versatile triangle')
else:
    print('Isosceles triangle')

# По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.

x1, y1 = map(lambda x: float(x), input("Enter coordinate value of the first point(e.g. 2 7 or -2 -7: ").split())
x2, y2 = map(lambda y: float(y), input("Enter coordinate value of the second point(e.g. 2 7 or -2 -7: ").split())

k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2

print(f'y = {k:.2f} * x + {b:.2f}')

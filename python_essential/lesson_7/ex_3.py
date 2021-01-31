# Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
# инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
# перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление
# (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
# обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения
# до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
# нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
# двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
# ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный
# метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.

class Cell:

    def __init__(self, count: int):
        self.cell_count = int(count)

    def __add__(self, other):
        if isinstance(self, Cell) and isinstance(other, Cell):
            self.cell_count += other.cell_count
            return self.cell_count

    def __sub__(self, other):
        if isinstance(self, Cell) and isinstance(other, Cell):
            if self.cell_count - other.cell_count > 0:
                self.cell_count -= other.cell_count
                return self.cell_count
            else:
                return 'You can\'t  kill all cells, it will destroy us.'

    def __mul__(self, other):
        if isinstance(self, Cell) and isinstance(other, Cell):
            self.cell_count *= other.cell_count
            return self.cell_count

    def __truediv__(self, other):
        if isinstance(self, Cell) and isinstance(other, Cell):
            try:
                self.cell_count = round(self.cell_count / other.cell_count)
                return self.cell_count
            except ZeroDivisionError as e:
                return f'{e} is redundant'

    def make_order(self, amount):
        for i in range(self.cell_count // amount):
            print('*' * amount)
        print('*' * (self.cell_count % amount))


cell = Cell(23)
cell_two = Cell(2)
print(cell - cell_two)
print(cell + cell_two)
print(cell * cell_two)
print(cell / cell_two)

cell.make_order(5)




# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.
from typing import List


class Matrix:

    def __init__(self, def_list: List[List]):
        self.matrix = def_list
        self.tmp_matrix = [[] for _ in self.matrix]

    def __str__(self):
        return f'{self.matrix}'

    def __add__(self, other):
        for deep in range(len(self.matrix)):
            for idx in range(len(other.matrix[0])):
                self.tmp_matrix[deep].append(self.matrix[deep][idx] + other.matrix[deep][idx])

        return self.tmp_matrix

    # def __add__(self, other):
    #     return [[self.matrix[deep][idx] + other.matrix[deep][idx] for idx in range(len(self.matrix[0]))]
    #             for deep in range(len(other.matrix))]




m_1 = [
    [1, 2, 3],
    [2, 4, 6]
]

m_2 = [
    [1, 2, 3],
    [2, 4, 6]
]

m_one = Matrix(m_1)
m_two = Matrix(m_2)

print(m_one)
print(m_one + m_two)
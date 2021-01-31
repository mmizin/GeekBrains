# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
# одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
# соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
# классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC


class Clothes(ABC):

    def __init__(self, vol, height):
        self.vol = vol
        self.height = height

    @property
    def tissue_consumption(self):
        if isinstance(self, Coat):
            return self.vol / 6.5 + 0.5
        elif isinstance(self, Suit):
            return 2 * self.height + 0.3

    def __add__(self, other):
        return self.tissue_consumption + other.tissue_consumption


class Coat(Clothes):
    pass


class Suit(Clothes):
    pass


coat = Coat(3, 4)
suit = Suit(3, 4)

print(coat.tissue_consumption)
print(suit.tissue_consumption)

print(coat + suit)

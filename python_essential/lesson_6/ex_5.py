# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать
# переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
# Starting drawing with a pencil

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Starting drawing')


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Starting drawing the {self.title} with a {self.__class__.__name__}')


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Starting drawing the {self.title} with a {self.__class__.__name__}')


class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Starting drawing the {self.title} with a {self.__class__.__name__}')


pencil = Pencil('auto-portret')
pencil.draw()
print()

pen = Pen('nature')
pen.draw()
print()

handle = Handle('landscape')
handle.draw()
print()

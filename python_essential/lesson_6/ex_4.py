# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    town_car_speed = 60
    work_car_speed = 40

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('The car start moving')

    def stop(self):
        print('The car stop moving')

    def turn(self, direction):
        print(f'The car turned {direction}')

    def show_speed(self):
        print(f'Current speed of {self.name} is {self.speed}')


class TownCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of {self.name} is {self.speed}')
        if self.speed > self.town_car_speed:
            print(f'You have exceed the speed. Appropriate speed for your car type is {self.town_car_speed} km')


class SportCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of {self.name} is {self.speed}')
        if self.speed > self.work_car_speed:
            print(f'You have exceed the speed. Appropriate speed for your car type is {self.work_car_speed} km')


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(61, 'blue', 'town_car')

town_car.go()
town_car.turn('right')
town_car.show_speed()
town_car.stop()
print()

sport_car = SportCar(120, 'yellow', 'bamblbi')

sport_car.go()
sport_car.turn('left')
sport_car.show_speed()
sport_car.stop()
print()

work_car = WorkCar(40, 'red', 'work_car')

work_car.go()
work_car.turn('right')
work_car.show_speed()
work_car.stop()
print()

police_car = PoliceCar(140, 'white-black', 'police_car')

police_car.go()
police_car.turn('right')
police_car.show_speed()
police_car.stop()
print()

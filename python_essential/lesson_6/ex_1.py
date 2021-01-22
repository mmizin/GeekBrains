# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
# — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep

CRED = '\033[91m'
CYELLOW = '\33[33m'
CGREEN = '\33[92m'
CEND = '\033[0m'


class TrafficLight:
    __color = str

    def running(self):
        __color = 'RED'
        for sec in range(0, 7):
            print(f'{CRED}STOP\nTraffic light is {__color}{CEND}')
            sleep(1)

        __color = 'YELLOW'
        for sec in range(0, 2):
            print(f'{CYELLOW}READY\nTraffic light is {__color}{CEND}')
            sleep(1)

        __color = 'GREEN'
        for sec in range(0, 10):
            print(f'{CGREEN}GO\nTraffic light is {__color}{CEND}')
            sleep(1)


TrafficLight().running()

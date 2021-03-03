# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
# года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
import datetime


class Date:
    date = ''

    def __init__(self, date):
        Date.date = date

    @classmethod
    def transform_date(cls):
        return int(datetime.datetime.strptime(cls.date, '%d-%m-%Y').strftime("%s"))

    @staticmethod
    def date_validation(date):
        try:
            datetime.datetime.strptime(date, '%d-%m-%Y')
        except ValueError:
            raise ValueError('Incorrect data format, should be: DD-MM-YYYY')


d = Date('01-11-2021')
print(d.transform_date())
d.date_validation('31-13-2021')

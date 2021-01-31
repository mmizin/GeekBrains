# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.

class CustomDivisionByZeroError(Exception):

    def __init__(self):
        self.text = 'Division by zero is redundant!'
        super().__init__(self.text)


try:
    num_one = int(input('Enter a number: '))
    num_two = int(input('Enter a number to divide on: '))

    if num_two == 0:
        raise CustomDivisionByZeroError

    print(num_one / num_two)
except CustomDivisionByZeroError as e:
    print(e)


# В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10
# попыток. После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то,
# что загадано. Если за 10 попыток число не отгадано, вывести ответ.

from random import randrange

random = randrange(0, 101)
count = 10
print(random)

while True:
    if count != 0:
        num = int(input(f'Try to the guess number between 0 - 100, you have {count} attempts: '))
        if num == random:
            print(f'You are right. The wanted number was {random}.')
            break
        elif num > random:
            print('Enter the number smaller than the previous one.')
            count -= 1
        else:
            print('Enter the number bigger than the previous one.')
            count -= 1
    else:
        print('Unfortunately, you haven\'t guessed the number.')
        break

# Определить, является ли год, который ввел пользователь, високосным или не високосным.

year = int(input('Enter please year: '))

if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
    print('The year is leap')
else:
    print('The year is not leap')

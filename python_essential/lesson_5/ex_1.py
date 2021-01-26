# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

input_data = list()

while True:
    input_data.append(input('Enter data. Press enter button without any data if finished: ').strip())
    if not input_data[-1]:
        input_data.pop(-1)
        break

if input_data:
    with open('user_data.txt', 'w') as f:
        f.write('\n'.join(input_data))
else:
    print("You have not passed any arguments. Please try to rerun and pass some arguments.")

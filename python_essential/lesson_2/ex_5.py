
while True:
    try:
        input_num = int(input('Enter your number: '))
        if input_num:
            my_list = [7, 5, 3, 3, 2, input_num]
            my_list.sort(reverse=True)
            print(my_list)
            break
    except ValueError:
        pass

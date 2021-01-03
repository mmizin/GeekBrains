STOP_SIGN = '$'
total = 0


def get_params():
    stop_exist = False

    while True:
        input_data = list(map(lambda x: x.strip(), input('Enter numbers separated by ",". If you have finished, '
                                                         'enter "$" : ').split()))
        if STOP_SIGN in input_data:
            input_data.remove(STOP_SIGN)
            stop_exist = True
        try:
            if input_data or STOP_SIGN:
                return list(map(lambda x: int(x), input_data)), stop_exist
            else:
                print('You did not pass any parameters')
        except ValueError:
            print('You have passed not a number.')


while True:
    params, stop = get_params()
    total += sum(params)

    if stop:
        print(total)
        break
    print(total)


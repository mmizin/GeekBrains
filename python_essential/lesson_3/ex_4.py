def my_func_pow(x, y):
    return x ** y


def my_func_pow_loop(x, y):
    y *= -1
    tmp = x
    if y > 0:
        for i in range(y-1):
            x = x * tmp
        return 1 / x
    else:
        return 1


def get_r_num():

    while True:
        try:
            real_num = input('Enter real number: ').strip()
            real_num = float(real_num) if '.' in real_num else int(real_num)
            if real_num < 0:
                print(f'You have passed a negative real number "{real_num}" instead of positive, e.g "1 or 3.12! '
                      f'Please enter a positive real number.')
            else:
                return real_num
        except (ValueError, TypeError):
            print('You have passed not a real number. Please enter only real number, e.g "123 or 4.333"')


def get_z_num():

    while True:
        try:
            z_number = int(input('Enter an negative integer: ').strip())
            if z_number > 0:
                print(f'You have passed a positive integer "{z_number}" instead of negative, e.g "-1 or -123! '
                      f'Please enter an negative integer.')
            else:
                return z_number
        except (ValueError, TypeError):
            print('You have passed not an integer. Please enter only an integer, e.g "123 or  or -367"')


print(my_func_pow(get_r_num(), get_z_num()))
print(my_func_pow_loop(get_r_num(), get_z_num()))

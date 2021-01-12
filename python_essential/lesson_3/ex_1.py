def divide_num(num_o, num_t):
    return num_o / num_t


input_data = input('Pass two numbers e.g "4 2": ')
first_num, second_num = list(map(lambda x: int(x.strip(', ')),  input_data.split()))

try:
    res = divide_num(first_num, second_num)
    print(f'The division of {first_num} and {second_num} numbers equals: {res}')
except ZeroDivisionError as e:
    print(f'The {e} is strictly forbidden, please try again.')


def display_data(name=None, second_name=None, birth_year=None, city=None, email=None, phone_number=None):
    for k, v in dict(list(locals().items())[::-1]).items():
        print(f'{k}: {v}', end='; ')


l_parameters = ['name', 'second_name', 'birth_year', 'city', 'email', 'phone_number']
input_data = {}

for param in l_parameters:
    input_data.setdefault(param, input(f'Enter your {param}: ').strip())

for key, val in input_data.items():
    if not val:
        raise Exception(f'You din\'t pass {key} value. All parameters have to be passed.')


display_data(name=input_data.get('name'),
             second_name=input_data.get('second_name'),
             birth_year=input_data.get('birth_year'),
             city=input_data.get('city'),
             email=input_data.get('email'),
             phone_number=input_data.get('phone_number'))



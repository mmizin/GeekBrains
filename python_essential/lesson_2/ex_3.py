month = input('Enter number of the month: ')

while True:

    if month and month.isdigit():
        months = {
            'Winter': {
                12: 'December',
                1: 'January',
                2: 'February'
            },
            'Spring': {
                3: 'March',
                4: 'April',
                5: 'May'
            },
            'Summer': {
                6: 'June',
                7: 'July',
                8: 'August'
            },
            'Autom': {
                9: 'September',
                10: 'October',
                11: 'November'
            }
        }
        for year_part, l_months in months.items():
            for key, val in l_months.items():
                if key == int(month):
                    print(f'Your month is {val} which belong to the {year_part}.')

        list_months = ['January', 'February', 'March',
                       'April', 'May', 'June',
                       'July', 'August', 'September',
                       'October', 'November', 'December']

        print('------------ List variant --------------')

        if int(month) in range(0, 3) or int(month) == 12:
            print(f'Your month is {list_months[int(month)-1]} which belong to the Winter.')
        elif int(month) in range(2, 6):
            print(f'Your month is {list_months[int(month)-1]} which belong to the Spring.')
        elif int(month) in range(6, 10):
            print(f'Your month is {list_months[int(month)-1]} which belong to the Summer.')
        elif int(month) in range(10, 12):
            print(f'Your month is {list_months[int(month)-1]} which belong to the Autom.')

        break
    else:
        month = input('Enter number of the month: ')

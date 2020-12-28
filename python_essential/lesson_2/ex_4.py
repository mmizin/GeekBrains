string = input('Enter words, separated by space: ')

spl_string = list(map(lambda x: x.strip(), string.split(' ')))

for index, e in enumerate(spl_string, 0):
    print(f'{index}: {e[0:11]}')

# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

rnd_chr = int(input('Enter the letter number in alphabet: '))

res = rnd_chr + 96

print(f'The letter "{chr(res).upper()}{chr(res)}" is on the {rnd_chr} place of the alphabet')

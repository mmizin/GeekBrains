# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

chr_start = input('Enter first letter: ')
chr_end = input('Enter second letter: ')

first_chr_place_in_alph = ord(chr_start.lower()) - 96
second_chr_place_in_alph = ord(chr_end.lower()) - 96
chrs_between = second_chr_place_in_alph - first_chr_place_in_alph - 1

print(f'The letter {chr_start} is on the {first_chr_place_in_alph} place of the alphabet')
print(f'The letter {chr_end} is on the {second_chr_place_in_alph} place of the alphabet')
print(f'Letters count between {chr_start} and {chr_end} are {chrs_between}')

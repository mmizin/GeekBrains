# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

import googletrans

translator = googletrans.Translator()

with open('ex_4.txt', 'r') as f:
    text = f.read()

with open('ex_4_translated.txt', 'w') as f:
    f.write(translator.translate(text, dest='ru').text)
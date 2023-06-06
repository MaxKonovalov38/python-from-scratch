#!/usr/bin/python3
import googletrans
'''
Добавьте в скрипт переводчика немецкий и французский языки
'''
input_text = input('Введите фразу, которую нужно перевести: ')
lang = int(input('''Введите параметр перевода:
1 - на английский;
2 - на русский;
3 - на немецкий;
4 - на французкий.
>>> '''))

if lang == 1:
    translate_text = googletrans.Translator().translate(input_text, dest = 'en').text
elif lang == 2:
    translate_text = googletrans.Translator().translate(input_text, dest = 'ru').text
elif lang == 3:
    translate_text = googletrans.Translator().translate(input_text, dest = 'de').text
elif lang == 4:
    translate_text = googletrans.Translator().translate(input_text, dest = 'fr').text
else:
    translate_text = 'Вы ввели что-то не то!'

print(translate_text)
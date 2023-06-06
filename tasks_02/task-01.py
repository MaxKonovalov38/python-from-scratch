#!/usr/bin/python3
"""
Напишите программу, которая просит у пользователя ввода десяти чисел по отдельности, добавляет их в список,
а после этого сортирует данный список, и печатает его, умножив каждое число на 10
"""

list_number = []
new_list_number = []
input_number = 0

for x in range(10):
    input_number = int(input("Введите число, после нажмите Enter: "))
    list_number.append(input_number)


list_number.sort()
for i in list_number:
    new_list_number.append(i * 10)


print(new_list_number)
'''
Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона. 
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. 
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
'''

from random import random

a1 = int(input('Введите первое целое число > 0 (начало диапазона, от): '))
a2 = int(input('Введите второе целое число > 0 (конец диапазона, до): '))
r = int(random() * (a2 - a1 + 1)) + a1
print(f'В диапазоне от {a1} до {a2} получено случайное целое число - {r}')

a1 = float(input('Введите первое вещественное число > 0 (начало диапазона, от): '))
a2 = float(input('Введите второе вещественное число > 0 (конец диапазона, до): '))
r = random() * (a2 - a1) + a1
print(f'В диапазоне от {a1} до {a2} получено случайное вещественное число - {round(r,2)}')

a1 = input('Введите первый символ диапазона от "a" до "f" (ОТ): ')
a2 = input('Введите последний символ диапазона от "a" до "f" (ДО): ')
r = int(random() * (ord(a2) - ord(a1) + 1)) + ord(a1)
print(f'В диапазоне от "{a1}" до "{a2}" получен случайный символ - "{chr(r)}"')

""""
1. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

d = {'1': 'Winter', '2': 'Spring', '3': 'Summer', '4': 'Autumn'}
seasons = ['Winter', 'Spring', 'Summer', 'Autumn']
month = int(input('Enter the month as a number: '))
if month == 1 or month == 12 or month == 2:
    print('Result via dictionary: ' + d['1'])
    print('Result via list: ' + seasons[0])
if month == 3 or month == 4 or month == 5:
    print('Result via dictionary: ' + d['2'])
    print('Result via list: ' + seasons[1])
if month == 6 or month == 7 or month == 8:
    print('Result via dictionary: ' + d['3'])
    print('Result via list: ' + seasons[2])
if month == 9 or month == 10 or month == 11:
    print('Result via dictionary: ' + d['4'])
    print('Result via list: ' + seasons[3])
else:
    print('This month does not exist')
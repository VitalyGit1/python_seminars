"""
Задание 4. Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

steps = int(input('Enter number: '))

def sum_of_series(n):
    if n == 1:
        return 1
    else:
        return ((-1)*(n+1) * 0.5*(n-1)) + sum_of_series(n-1)

n = int(input("Введите количество элементов: "))
print(f"Количество элементов - {n}, их сумма - {sum_of_series(n)}")
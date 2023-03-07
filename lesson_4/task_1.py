"""
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются
в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества.
m - кол-во элементов второго множества. Затем пользователь вводит сами
элементы множеств.
"""

m1 = set(
    [int(x) for x in
     input("Enter numbers separated by spaces: ").split()])

m2 = set(
    [int(x) for x in input("Enter numbers separated by spaces: ").split()])

res = set()

for i in m1:
    if i in m2:
        res.add(i)

resList = list(res)
resList.sort()
print(resList)

#  Фуфло

# set_1 = set()
# set_2 = set()
#
# a = [int(x) for x in input().split()]
# k = set(a)
# for i in k:
#     set_1.add(i)
#
# b = [int(x) for x in input().split()]
# k1 = set(b)
# for i in k1:
#     set_2.add(i)
#
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#     print(i, end=' ')

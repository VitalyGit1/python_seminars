# name = input('Введите ваше имя: ')
# password = input('Введите ваш пароль: ')
# age = input('Введите ваш возраст: ')
# print('Ваши данные для входа в аккаунт: ', 'Имя: ' + name + ',',
#       'Пароль: ' + password + ',', 'Возраст: ' + age)

# 2
# time = int(input("Введите время в секундах: "))
# hours = time // 3600
# minutes = (time - hours * 3600) // 60
# seconds = time - (hours * 3600 + minutes * 60)
# print(f"Время в формате чч:мм:сс   {hours} : {minutes} : {seconds}")

# 3
# n = int(input("Введите число - "))
# total = (n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))
# print("Сумма чисел n + nn + nnn - %d" % total)

# 4
profit = float(input("Введите выручку фирмы "))
costs = float(input("Введите издержки фирмы "))
if profit > costs:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила "
          f"{profit / costs:.2f}")
    workers = int(input("Введите количество сотрудников фирмы "))
    print(
        f"прибыль в расчете на одного сторудника сотавила "
        f"{profit / workers:.2f}")
elif profit == costs:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")

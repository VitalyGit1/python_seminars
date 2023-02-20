# name = input('Введите ваше имя: ')
# password = input('Введите ваш пароль: ')
# age = input('Введите ваш возраст: ')
# print('Ваши данные для входа в аккаунт: ', 'Имя: ' + name + ',',
#       'Пароль: ' + password + ',', 'Возраст: ' + age)

# 2
time = int(input("Введите время в секундах: "))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"Время в формате чч:мм:сс   {hours} : {minutes} : {seconds}")

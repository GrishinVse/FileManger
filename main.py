import platform
import os
"""
Главный файл для запуска всего приложения

1. Тут написаны сообщения для пользователя.
2. Весь файл - работа с одним вводом, который отвечает за выбор ОС.
3. После ввода числа идет считывание и выполнение того файла, который работает с той или иной ОС.
4. Контроль за правильным запуском идет через функцию platform.system(), которая возвращает название текущей ОС.
5. Если пользователь в поле ввода ввел неправильное значение, то выводится сообщение об этом.
"""
print('{:*^30}'.format('Welcome!'))
print('\nChoose OS to work with:\n')
print('1.Windows')
print('2.Linux OS\n')
print('{:*^30}'.format('>EXIT<') + '\n')

while True:
    result = input("Choose one of the options: ")
    if result.strip() == '1':
        if platform.system() == "Windows":
            os.system("winmanager.py")
            break
        else:
            print("You are not in Windows OS!")
    elif result.strip() == '2':
        if platform.system() == "Linux":
            exec(open("linuxmanager.py").read())
            break
        else:
            print("You are not in Linux OS!")
    if result.strip().lower() == "exit":
        break
    else:
        print("Wrong option selected! Please try again.\n")

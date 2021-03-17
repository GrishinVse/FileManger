import os
import platform

"""
Код Linux части

Как и для винды здесь есть 6 функций:
    > открыть файл/папку
    > записать в файл
    > создать файл/папку
    > скопировать
    > удалить
    > переименовать

Все работает достаточно просто: на выбор предлагается команда, дальше идет вывод всех файлов списком в терминал.

Список генерится функцией listDirectories() (она написана ниже), дальше пользователь вводит путь до файла, если он корректен, то происходит
переход в нужную папку, чтобы там уже что-то делать. Правильность ввода имен файлов и папок идет через библиотеку os, 
как и выполнение всех команд.

Сами по себе команды это системные команды терминала cat, cd, mv и т.д. которые надо правильным образом дать в систему.

Все возможные ошибки прописаны внутри исключений и выводятся в консоль.
"""

print('{:*^40}'.format('Welcome to the File Manager on ' + platform.system()) + "\n")

list_of_commands = ["1", "2", "3", "4", "5", "6", "exit"]

def listDirectories():
    listdir = os.listdir(os.getcwd())
    for x in listdir:
        print(x)


while True:
    print('{:*^30}'.format('MAIN MENU') + '\n')
    print("1.Open files/folders \n2.Write into file \n3.Create file/dir \n4.Copy and Paste \n5.Delete\n6.Rename\n>EXIT<")
    need_com = input("Choose option: ")
    if need_com == "1":
        while True:
            listDirectories()
            need_dir = input("Type folder path or command: ")
            if need_dir.lower() == 'back':
                os.chdir('..')
            elif need_dir.lower() == 'exit':
                break
            elif os.path.isdir(need_dir):
                os.popen('cd ' + need_dir)
                os.chdir(os.path.expandvars(need_dir))
                listDirectories()
            elif os.path.isfile(need_dir):
                os.system('cat ' + need_dir)
            else:
                print("Folder not found")
    if need_com == "2":
        while True:
            res = input("Type file path: ")
            if res.lower() == "exit":
                break
            elif os.path.isfile(res):
                write_res = input("Type text: ")
                os.system('echo ' + '"' + write_res + '" ' + '>> ' + res)
            else:
                print("File not found")
    if need_com == '3':
        while True:
            res = input("Type file path: ")
            if res.lower() == "exit":
                break
            elif os.path.isdir(res):
                os.popen('cd ' + res)
                os.chdir(os.path.expandvars(res))
                file_or_dir = input("You want to create dir or file? ")
                if file_or_dir == 'file':
                    name_input = input("Type filename: ")
                    os.system('touch ' + name_input)
                if file_or_dir == 'dir':
                    name_input = input("Type dirname: ")
                    os.system('mkdir ' + name_input)
                    listDirectories()
            else:
                print("Incorrect file path")
    if need_com == "4":
        while True:
            res = input("Type file path: ")
            if res.lower() == "exit":
                break
            elif os.path.isdir(res):
                os.chdir(os.path.expandvars(res))
                need_file = input("Type filename: ")
                if os.path.isfile(need_file):
                    copy_dir = input("Type path to copy: ")
                    if os.path.isdir(copy_dir):
                        os.system('cp ' + need_file + " " + copy_dir)
                        listDirectories()
            else:
                print("Incorrect dir input")
    if need_com == "5":
        while True:
            res = input("Type file path: ")
            if res.lower() == "exit":
                break
            elif os.path.isdir(res):
                os.chdir(os.path.expandvars(res))
                listDirectories()
                need_file = input("Type filename to delete: ")
                if os.path.isfile(need_file):
                    os.system('rm ' + need_file)
                else:
                    print("It is not a file")
            else:
                print("Incorrect file path")
    if need_com == "6":
        while True:
            res = input("Type file path: ")
            if res.lower() == "exit":
                break
            elif os.path.isdir(res):
                os.popen('cd ' + res)
                listDirectories()
                res2 = input("Type filename: ")
                if os.path.isfile(res2):
                    res3 = input("Type new filename: ")
                    os.system('mv ' + res2 + " " + res3)
                    listDirectories()
            else:
                print("file not found")
    if need_com.lower() == "exit":
        break
    if not (need_com in list_of_commands):
        print("Wrong input value")
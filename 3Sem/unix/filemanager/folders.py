import os
import shutil
import configparser
config = configparser.ConfigParser()
config.read('settings.ini')
if not os.path.isdir(config['main direcroty']['name']):
    os.mkdir(config['main direcroty']['name'])
os.chdir(config['main direcroty']['name'])
def creation():
    new_folder_name= input('Введите имя папки: ')
    while True:
        try:
            os.mkdir(new_folder_name)
            break
        except FileExistsError and NameError:
            new_folder_name = input('такой файл уже существует или символы недоступны, попробуйте снова, -1 для выхода: ')
            if new_folder_name == "-1":
                break

def delete():
    print(os.listdir())
    name_of_dir = input("Введите имя папки для удаления ")
    try:
        os.remove(name_of_dir)
    except NameError:
        print('Name Error')
    except FileNotFoundError:
        print('File not found')
def movement():
    #print(os.listdir(),end="")
    directories=[d for d in os.listdir(os.getcwd()) if os.path.isdir(d)]
    directories.append('назад')
    print(directories)
    move = (input('Куда осуществить перемещение? '))
    while True:
        if move == "назад":
            os.chdir('..')
            if os.path.isdir('Folder'):
                print("Атата, туда нельзя")
                os.chdir('Folder')
            break
        else:
            try:
                os.chdir(move)
            except NameError:
                print("Name Error")
            except FileNotFoundError:
                print("File not found")
            break

def create_file():
    name_of_file = input("Введите имя файла с расширением")
    try:
        file = open(name_of_file,"w")
        file.close()
    except NameError:
        print("Ошибка ввода")
    except FileExistsError:
        print("Такой файл существует")

def writing():
    name_of_file = input("Введите имя файла без расширения ")
    try:
        file = open(f"{name_of_file}.txt","w")
        file.write(input("Что написать в файл? "))
    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("U can't do that")

def reader():
    name_of_file = input("Введите имя файла без расширения ")
    try:
        with open(f"{name_of_file}.txt","r") as f:
            f.read()
            f.close()
    except FileNotFoundError:
        print("No file Found")

def remover():
    print(os.listdir())
    name_of_file = input("Введите имя файла с расширением")
    try:
        os.remove(name_of_file)
    except NameError:
        print("Name Error")
    except FileNotFoundError:
        print("File not Found")

def copy():
    name_of_file = input("Введите имя файла с расширением")
    change = input("Введите полный путь куда хотите скопировать файл")
    try:
        shutil.copy(name_of_file,change)
    except NameError:
        print("Name Error")
    except FileNotFoundError:
        print('No File Exists')

def mover():
    print(os.listdir())
    name_of_file = input('Введите имя файла с расширением ')
    where = input('Введите полный путь, куда переместить файл ')
    try:
        os.replace(name_of_file,where)
    except NameError:
        print('Name Error')
    except FileNotFoundError:
        print('No file found')
    except NotADirectoryError:
        print("Can\'t place here")

def name_changer():
    print(os.listdir())
    name_of_file = input('Какой файл переименовать с расширением')
    new_name = input('Введите новое имя с расширением')
    try:
        os.rename(name_of_file,new_name)
    except FileNotFoundError:
        print('File not found')
    except NameError:
        print('Can\'t use that name')

while True:
    print(" 1) Создание папки (с указанием имени) \n 2) Удаление папки по имени \n 3) Перемещение между папками (в пределах рабочей папки) "
          "- заход в папку по имени, выход на уровень вверх \n 4) Создание пустых файлов с указанием имени "
          "\n 5) Запись текста в файл \n 6) Просмотр содержимого текстового файла \n 7) Удаление файлов по имени "
          "\n 8) Копирование файлов из одной папки в другую \n 9) Перемещение файлов \n 10) Переименование файлов."
          "\n 0) Закончить Работу с файлами \n -1) Где я и что вокруг?")

    DO = input("Какую операцию желаете выполнить? " )

    if DO=="0":
        break
    elif DO=="1":
        creation()
    elif DO=="2":
        delete()
    elif DO=="3":
        movement()
    elif DO=="4":
        create_file()
    elif DO=="5":
        writing()
    elif DO=="6":
        reader()
    elif DO=="7":
        remover()
    elif DO=="8":
        copy()
    elif DO=="9":
        mover()
    elif DO=="10":
        name_changer()
    elif DO=='-1':
        print(os.getcwd())
        print(os.listdir())
    else:
        print("Не в списке действий, попробуйте еще раз")
import os
import shutil

while True:
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. выход')

    choice = input('Выберите пункт меню ')
    if choice == '1':
        nameFolder=input("Ввведите название папки")
        if not os.path.exists(nameFolder):
            os.mkdir(nameFolder)
        if os.path.exists(nameFolder):
            print("Такая папка уже есть")
    elif choice == '2':
        nameFolder = input("Ввведите название папки/файла")
        os.rmdir(nameFolder)
    elif choice == '3':
        print("1. Скопировать файл")
        print("2. Скопировать папку")
        choice = input('Выберите пункт меню ')
        if choice == '1':
            nameFile = input("Ввведите название файла")
            newnameFile = input("Ввведите новое название файла")
            if os.path.exists(f'{nameFile}.py'):
                shutil.copy(f'{nameFile}.py', f'{newnameFile}.py')
        if choice == '2':
            nameFolder = input("Ввведите название папки")
            newnameFolder = input("Ввведите новое название папки")
            if os.path.exists(nameFolder):
                 shutil.copytree(nameFolder, newnameFolder)
    elif choice == '4':
        print(os.listdir())
    elif choice == '5':
        f=[]
        for (dirpath, dirnames, filenames) in os.walk('console_file_manager'):
            f.extend(filenames)
        print(f)

    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')

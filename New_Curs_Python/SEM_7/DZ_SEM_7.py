# Напишите функцию группового переименования файлов.
# Она должна:
# - принимать параметр желаемое конечное имя файлов. При переименовании в
# конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла. Переименование должно
# работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени. Например для
# диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано.
# Далее счётчик файлов и расширение.


import os


def rename_files(path, new_filename, count_numbers, ext_for_rename, new_ext,
                 start, stop):

    for i, f in enumerate(os.listdir(path)):
        word, ext = f.split('.')
        print(word)
        # for j in word:
        if start == stop:
            if new_filename == "":
                new_filename = 'new_name_'
            if ext == ext_for_rename or ext_for_rename == 'txt':
                if count_numbers == 1:
                    if i < 10:
                        new_name = new_filename + "0" + str(i) + '.' + new_ext
                    else:
                        new_name = new_filename + str(i) + '.' + new_ext
                elif count_numbers == 2:
                    if i < 10:
                        new_name = new_filename + "00" + str(i) + '.' + new_ext
                    elif 10 <= i < 100:
                        new_name = new_filename + "0" + str(i) + '.' + new_ext
                    else:
                        new_name = new_filename + str(i) + '.' + new_ext
                else:
                    new_name = new_filename + str(i) + '.' + new_ext
                print(f'Файл {f} переименован в {new_name}')
                os.rename(path + '/' + f, path + '/' + new_name)
        else:
            if start > stop:
                start, stop = stop, start
            if ext == ext_for_rename or ext_for_rename == 'txt':
                if count_numbers == 1:
                    if i < 10:
                        new_name = word[start:stop] + \
                            new_filename + "0" + str(i) + '.' + new_ext
                    else:
                        new_name = word[start:stop] + \
                            new_filename + str(i) + '.' + new_ext
                elif count_numbers == 2:
                    if i < 10:
                        new_name = word[start:stop] + \
                            new_filename + "00" + str(i) + '.' + new_ext
                    elif 10 <= i < 100:
                        new_name = word[start:stop] + \
                            new_filename + "0" + str(i) + '.' + new_ext
                    else:
                        new_name = word[start:stop] + \
                            new_filename + str(i) + '.' + new_ext
                else:
                    new_name = word[start:stop] + \
                        new_filename + str(i) + '.' + new_ext
                print(f'Файл {f} переименован в {new_name}')
                os.rename(path + '/' + f, path + '/' + new_name)


def input_new_name():
    ansewer = input('Введите 1 если вы хотите назначить новое имя файлам:')
    if ansewer == '1':
        new_filename = str(input("Введите новое название для файлов : "))
    else:
        new_filename = ''
    return new_filename


def count_num():
    ansewer = input(
        'Введите 1 если хотите задать количество цифр в порядковом номере :')
    if ansewer == '1':
        count_numbers = int(input("Введите количество цифр от 1 до 2: "))
        if count_numbers > 2:
            count_numbers = 0
    else:
        count_numbers = 0
    return count_numbers


def input_ext():
    ansewer = input(
        'Введите 1 если хотите выбрать расширение файлов для переименования:')
    if ansewer == '1':
        ext_for_rename = str(
            input("Введите расширение для переименования файлов : "))
    else:
        ext_for_rename = 'txt'
    return ext_for_rename


def choice_ext(ext_for_rename):
    ansewer = input(
        'Введите 1 если для выбора нового расширение переименнующихся файлов:')
    if ansewer == '1':
        new_ext = str(input("Введите новое расширение для файлов : "))
    else:
        new_ext = ext_for_rename
    return new_ext


def diapason_old_name():
    ansewer = input(
        'Введите 1 если для выбора диапазона неизменяемых символов в имени:')
    if ansewer == '1':
        start = int(input("Введите начальное значение диапазона : "))
        stop = int(input("Введите конечное значение диапазона : "))
    else:
        start = 0
        stop = 0
    return start, stop


if __name__ == '__main__':

    DIRECTORI = 'C:/Users/user/Desktop/git edukation/PythonKurs/\
                                    New_Curs_Python/SEM_7/testt'
    new_filename = input_new_name()
    count_numbers = count_num()
    ext_for_rename = input_ext()
    new_ext = choice_ext(ext_for_rename)
    start, stop = diapason_old_name()
    rename_files(DIRECTORI, new_filename, count_numbers,
                 ext_for_rename, new_ext, start, stop)

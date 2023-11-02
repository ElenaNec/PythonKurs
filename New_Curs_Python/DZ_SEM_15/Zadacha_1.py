# Возьмите любые 1-3 задания из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки
# с передачей параметров.
#  Взята последняя задача из семинара 15

import logging

import pathlib
from collections import namedtuple

import argparse

FORMAT = '{levelname}, {asctime}, {msg}'

logging.basicConfig(format=FORMAT, style='{', filename='logs.log',
                    filemode='w', encoding='utf-8', level=logging.ERROR)
logger = logging.getLogger(__name__)


def log_dec(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(
                f'Ошибка {e} в функции {func.__name__} при {args}, {kwargs}')
        return None
    return wrapper


DIRSUBJECT = namedtuple("DIRSUBJECT", ["file_name", "ext", "flag", "name_dir"])


@log_dec
def dir_info(path):
    path = pathlib.Path(path)
    new_list = []
    for file in path.iterdir():
        new_list.append(DIRSUBJECT(file.name, file.suffix,
                        file.is_dir(), file.parent))
    return new_list


def par():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", default="C:/Users/user/Desktop/\
            git edukation/PythonKurs/New_Curs_Python/SEM_2/Zadacha_1.py")
    args = parser.parse_args()
    return dir_info(f'{args.file}')


print(par())

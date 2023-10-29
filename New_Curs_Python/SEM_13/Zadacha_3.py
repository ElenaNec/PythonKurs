# Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный идентификатор
# и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные
# в свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.


import json


class User:
    def __init__(self, name, id, lvl):
        self.name = name
        self.id = id
        self.lvl = lvl

    def __repr__(self) -> str:
        return f'User({self.name}, {self.id}, {self.lvl})'


def read(file_name):
    new_set = set()
    with open(file_name, "r")as f:
        data = json.load(f)
    for lvl, user in data.items():
        for id, name in user.items():
            new_set.add(User(name, id, lvl))
    return new_set


def data(name: str, id: str, level: str, file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            users = json.load(f)
    except FileNotFoundError:
        users = {'1': {}, '2': {}, '3': {},
                 '4': {}, '5': {}, '6': {}, '7': {}}
    users[level][id] = name
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False)


def request(file_name):
    while True:
        name = input('Введите имя: ')
        id = input('Введите id: ')
        level = input('Введите уровень: ')
        data(name, id, level, file_name)


# request('users1.json')
print(read('users1.json'))

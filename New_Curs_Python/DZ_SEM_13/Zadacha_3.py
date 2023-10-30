# В организации есть два типа людей: сотрудники и обычные люди.
# Каждый человек (и сотрудник, и обычный) имеет следующие атрибуты:

# Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка,
# не пустая)
# Возраст (целое положительное число) Сотрудники имеют также уникальный
# идентификационный номер (ID), который должен быть шестизначным положительным
# целым числом.

# Ваша задача:

# Создать класс Person, который будет иметь атрибуты и методы для
# управления данными о людях (Фамилия, Имя, Отчество, Возраст).
# Класс должен проверять валидность входных данных и генерировать
# исключения InvalidNameError и InvalidAgeError, если данные неверные.

# Создать класс Employee, который будет наследовать класс Person и добавлять
# уникальный идентификационный номер (ID). Класс Employee также должен
# проверять валидность ID и генерировать исключение InvalidIdError,
# если ID неверный.

# Добавить метод birthday в класс Person, который будет увеличивать
# возраст человека на 1 год.

# Добавить метод get_level в класс Employee, который будет возвращать
# уровень сотрудника на основе суммы цифр в его ID (по остатку от деления на 7)

# Создать несколько объектов класса Person и Employee с разными данными
# и проверить,
# что исключения работают корректно при передаче неверных данных.

from random import randint


class InvalidNameError(ValueError):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f'Invalid name: {self.text}. Name should be a non-empty string.'


class InvalidAgeError(ValueError):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'Invalid age: {self.number}. Age should be a positive integer.'


class InvalidIdError(ValueError):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'Invalid id: {self.number}. Id should be a 6-digit positive integer between 100000 and 999999.'


class Person:
    def __init__(self, surname: str, name: str, patronymic: str, age: int):
        if not isinstance(surname, str) or len(surname.strip()) == 0:
            raise InvalidNameError(surname)
        elif not isinstance(name, str) or len(name.strip()) == 0:
            raise InvalidNameError(name)
        elif not isinstance(patronymic, str) or len(patronymic.strip()) == 0:
            raise InvalidNameError(patronymic)
        elif not (isinstance(age, int) or isinstance(age, float)) or age <= 0:
            raise InvalidAgeError(age)
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.__age = age

    def birthday(self):
        self.__age += 1

    def get_age(self):
        return self.__age

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic} {self.__age}"


class Employee(Person):
    def __init__(self, name, second_name, patronymic, age, id):
        super().__init__(name, second_name, patronymic, age)
        if not isinstance(id, int) and not (100_000 <= id <= 999_999):
            raise InvalidIdError(id)
        self.id = id

    def get_level(self):
        self.lvl = self.id % 7


# person = Person("Alice", "Smith", "Johnson", 25)
# print(person.get_age())
# person = Person("Ivanov", "John", "Doe", 30)
# print(person)

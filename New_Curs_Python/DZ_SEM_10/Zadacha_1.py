# Создайте базовый класс Animal, который имеет атрибут name, представляющий имя животного.

# Создайте классы Bird, Fish и Mammal,
# которые наследуются от базового класса Animal и добавляют дополнительные атрибуты и методы:

# Bird имеет атрибут wingspan (размах крыльев) и метод wing_length,
# который возвращает длину крыла птицы.

# Fish имеет атрибут max_depth (максимальная глубина обитания) и метод depth,
# который возвращает категорию глубины рыбы (мелководная, средневодная, глубоководная) в зависимости от значения max_depth.

# Mammal имеет атрибут weight (вес) и метод category, который возвращает категорию млекопитающего (Малявка, Обычный, Гигант)
# в зависимости от веса.

# Создайте класс-фабрику AnimalFactory, который будет создавать экземпляры животных разных типов на основе переданного типа и параметров.
# Класс-фабрика должен иметь метод create_animal, который принимает следующие аргументы:

# animal_type (строка) - тип животного (один из: 'Bird', 'Fish', 'Mammal').
# *args - переменное количество аргументов, представляющих параметры для конкретного типа животного.
# Количество и типы аргументов могут различаться в зависимости от типа животного. Метод create_animal должен создавать
# и возвращать экземпляр животного заданного типа с переданными параметрами.


class Animals:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        return f"{self.name}"


class Bird(Animals):
    def __init__(self, name, wingspan):
        self.name = name
        self.wingspan = wingspan
        
    def wing_length(self):
        return f"{self.wingspan}"


class Fish(Animals):
    def __init__(self, name, max_depth):
        self.name = name
        self.max_depth = max_depth
        
    def depth(self):
        '''категория глубины рыбы: мелководная(0-10), средневодная(11-200),
           глубоководная(201-далее)'''
        return f'{self.name} {self.color}'


class Mammal(Animals):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def category(self):
        '''Категория млекопитающего: Малявка(0-10), Обычный(11-100),
           Гигант(101-далее)'''
        
        return f'{self.name} {self.weight}'


class AnimalFactory(Animals):
    def __init__(self, type_an, name, *args):
        self.name = name
        self.type_an = type_an
                     
    def create_animal(self):
        if self.type_an = 'Bird':
            return Animals.
        
            
        type_a = 
        animal_type = animals_dict[type_a]
        return f'{self.name} {self.weight}'
    




# dog = Fish("овчарка", "+", "Рекс")
# print(dog.print_info())
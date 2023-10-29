# Создайте базовый класс Animal, который имеет атрибут name, 
# представляющий имя животного.

# Создайте классы Bird, Fish и Mammal,
# которые наследуются от базового класса Animal и добавляют дополнительные
# атрибуты и методы:

# Bird имеет атрибут wingspan (размах крыльев) и метод wing_length,
# который возвращает длину крыла птицы.

# Fish имеет атрибут max_depth (максимальная глубина обитания) и метод depth,
# который возвращает категорию глубины рыбы (мелководная, средневодная,
# глубоководная) в зависимости от значения max_depth.

# Mammal имеет атрибут weight (вес) и метод category, который возвращает
# категорию млекопитающего (Малявка, Обычный, Гигант)
# в зависимости от веса.

# Создайте класс-фабрику AnimalFactory, который будет создавать экземпляры
# животных разных типов на основе переданного типа и параметров.
# Класс-фабрика должен иметь метод create_animal, который принимает
# следующие аргументы:

# animal_type (строка) - тип животного (один из: 'Bird', 'Fish', 'Mammal').
# *args - переменное количество аргументов, представляющих параметры для
# конкретного типа животного.
# Количество и типы аргументов могут различаться в зависимости от типа
# животного. Метод create_animal должен создавать
# и возвращать экземпляр животного заданного типа с переданными параметрами.


class Animals:
    def __init__(self, name):
        self.name = name


class Bird(Animals):
    def __init__(self):
        pass

    def wing_length(wingspan):
        wing = wingspan[0] / 2
        return print(f"{wing}")


class Fish(Animals):
    def __init__(self):
        pass

    def depth(max_depth):
        '''категория глубины рыбы: мелководная(0-10), средневодная(11-200),
           глубоководная(201-далее)'''
        if 0 < max_depth[0] <= 10:
            depth_fish = "Мелководная рыба"
        elif 11 < max_depth[0] <= 200:
            depth_fish = "Средневодная рыба"
        else:
            depth_fish = "Глубоководная рыба"
        return print(f'{depth_fish}')


class Mammal(Animals):
    def __init__(self):
        pass

    def category(weight):
        '''Категория млекопитающего: Малявка(0-10), Обычный(11-100),
           Гигант(101-далее)'''
        if 0 < weight[0] <= 10:
            category_mammal = "Малявка"
        elif 11 < weight[0] <= 100:
            category_mammal = "Обычный"
        else:
            category_mammal = "Гигант"
        return print(f'{category_mammal}')


class AnimalFactory(Animals):
    def create_animal(type_an, name, *param):

        if type_an == 'Bird':
            return Bird.wing_length(param)
        elif type_an == 'Fish':
            return Fish.depth(param)
        elif type_an == 'Mammal':
            return Mammal.category(param)


# Создание экземпляров животных
animal1 = AnimalFactory.create_animal('Bird', 'Орел', 200)
animal2 = AnimalFactory.create_animal('Fish', 'Salmon', 50)
animal3 = AnimalFactory.create_animal('Mammal', 'Слон', 5000)

"""Функция нахождения мин и макс """
 
def min_and_max(iterable):
    min_value, max_value = float('inf'), float('-inf')
    for value in iterable:
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value
    return min_value, max_value 
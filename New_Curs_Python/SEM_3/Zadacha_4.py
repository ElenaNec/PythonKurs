# Создайте вручную список с повторяющимися элементами. 
# Удалите из него все элементы, которые встречаются дважды.

a = [1, 2, 3, 4, 4, 5, 6, 6, 7, 7, 8, 8, 9, 9, 0]
for i in a:
    if a.count(i) == 2:
        a.remove(i)
        a.remove(i)
print(a)
'''Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
Она растет на круглой грядке, причем кусты высажены только по окружности. 
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод 
– на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
собирает ягоды с этого куста и с двух соседних с ним.

Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки.'''

n = int(input("Введите количество кустов : "))

col = list(int(input(f"Введите количество ягод на {i} кусте : ")) for i in range(n))

#или так
# col = []
# for i in range(n):
#     x = int(input(f"Введите количество ягод на {i} кусте : "))
#     col.append(x)
    
rez = []
for i in range(len(col)-1):
    rez.append(col[i-1] + col[i] + col[i+1])
rez.append(col[-1] + col[-2] + col[0])
print(max(rez))
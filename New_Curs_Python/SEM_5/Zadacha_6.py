# Преобазовать задачу "таб умножения" из 1 семинара
# в генераторную строку

#  Выведите в консоль таблицу умножения от 2х2 до 9х10,
# как на школьной тетради

# for i in range(2, 10, 4):
#     for j in range(2, 11):
#         for k in range(i, i + 4):
#             print(f'{k:.>3} * {j: > 3} = {(k*j): >3}', end='\t')
# # форматирование строк :>3 - добавление пробела
#         print()
#     print()

res = ['\n'+'\t'.join([f'{k:>3} *{j:>3} ={(k * j):>3}'
                       for k in range(i, i + 4)])
       if i == 6 and j == 2 else '\t'.join([f'{k:>3} *{j:>3} ={(k * j):>3}'
                                            for k in range(i, i + 4)])
       for i in range(2, 10, 4)
       for j in range(2, 11)]

# print('\t'.join(res))


print(*res, sep='\n')

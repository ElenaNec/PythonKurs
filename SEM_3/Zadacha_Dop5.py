"""Как обращаться к эл-там списка"""

my_list = [1,2,'3','4345645ergd',5,
(23,34,45,56),
True, False,
{1,1,1,2,2,3,3},
{(22,): 1, (2.3,): [11,22,33,44], (3,): 111,
('one',): 111, (11,22,33,66): 'наш кортеж'}]

# print(my_list)
# print(my_list[0] *130)
# print(my_list[3].upper())
# print(my_list[5][2])
# print(my_list[9][2.3][2])
# print(my_list[9][(11,22,33,66)])
for key in my_list[9]:
    if 22 in key:
        print(f'кортеж - {key} : {my_list[9][key]}')
        print('в нашем кортеже есть 22')

    if 25 in key:
        print('в нашем кортеже ytn 25')
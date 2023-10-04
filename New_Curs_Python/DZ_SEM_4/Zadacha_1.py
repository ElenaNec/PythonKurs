# Напишите функцию для транспонирования матрицы.
# Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]


def transoprt_matrix(matrix: list[int]) -> list[int]:
    trans_matrix = [[0, 0], [0, 0], [0, 0]]
    for a in range(len(matrix)):
        for b in range(len(matrix[0])):
            trans_matrix[b][a] = matrix[a][b]
    return trans_matrix


matrix = [[2, 2, 3], [7, 5, 6]]
print(transoprt_matrix(matrix))

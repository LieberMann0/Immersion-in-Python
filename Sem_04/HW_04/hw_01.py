# Напишите функцию для транспонирования матрицы


# def matrix_transposition(matrix: list[str, int]) -> list[str, int]:

#     a = len(matrix[0])
#     b = len(matrix)
#     transpos = []

#     for i in range(a):
#         invert = []
#         for j in range(b):
#             invert.append(matrix[j][i])
#         transpos.append(invert)
#     return transpos


def matrix_transposition(matrix: list[str, int]) -> list[str, int]:
    new_array = [*zip(*matrix)]
    return new_array

my_matrix = [["A", "B", "C"], [1, 2, 3]]

print(matrix_transposition(my_matrix))

def show_matrix(matrix):
    for i in matrix:
        print(i)
    print()


def divide_line(line, j):
    div = line[j]
    for i in range(len(line)):
        line[i] /= div


def substract_line(first, second, j):
    div = second[j] / first[j]
    for i in range(len(second)):
        second[i] -= first[i] * div


matrix = [
    [1, 2, 4, -5],
    [-2, 1, -3, 10],
    [3, -2, -5, 3]
    #   x( -1, 2, -2 )
]
domatrix = []
n = len(matrix)
show_matrix(matrix)
for j in range(n):
    #   Сортировка по  главному элементу столбца
    for k in range(j, n):
        for i in range(j + 1, n):
            if abs(matrix[i - 1][j]) < abs(matrix[i][j]):
                mat = matrix[i - 1]
                matrix[i - 1] = matrix[i]
                matrix[i] = mat
    #   Делим строку на главный элемент
    divide_line(matrix[j], j)
    #   Приводим к нулю значения ниже главного элемента
    for k in range(j + 1, n):
        substract_line(matrix[j], matrix[k], j)
show_matrix(matrix)
#   Получили нашу матрицу
#   Находим вектор x
x = [0] * n
for i in range(n - 1, -1, -1):
    x[i] = matrix[i][n]
    for j in range(n - 1, i, -1):
        x[i] -= matrix[i][j]*x[j]
#   Выводим вектор x без учета погрешности
print(*x)
# Теперь ищем эпсилон
e = [0]*n

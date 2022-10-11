class Reader:
    file_text = []

    def __init__(self, src):
        self.file = open(src, 'r')

    def src_read(self):
        for line in self.file:
            self.file_text.append(line)
        return self.file_text


# file1 = Reader('E:/Методы вычислений/Matrix.txt')
# print(*file1.src_read())

matrix = [
    [2.6, -4.5, -2.0, 19.07],
    [3, 3, 4.3, 3.21],
    [-6, 3.5, 3, -18.25]
]

for i in matrix:
    print(i)

n = len(matrix)
for i in range(n):
    if matrix[i][i] == 0:
        print('Элемент на главной диагонали равен нулю')
        n = 0

if n:
    print()

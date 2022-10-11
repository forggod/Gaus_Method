class Reader:
    file_text = []

    def __init__(self, src):
        self.file = open(src, 'r')

    def src_read(self):
        for line in self.file:
            self.file_text.append(line)
        return self.file_text


# file1 = Reader('Matrix.txt')
# print(*file1.src_read())

def zerodation(matrix, row, k, n):  # Привидение к треугольному виду
    max = row[0]
    for i in row:
        if max < i:
            max = i
    # for el in row:



matrix = [
    [2.6, -4.5, -2.0, 19.07],
    [3, 3, 4.3, 3.21],
    [-6, 3.5, 3, -18.25]
]
zmatrix = []

for i in matrix:
    print(i)

n = len(matrix)
for i in range(n):
    if matrix[i][i] == 0:
        print('Элемент на главной диагонали равен нулю')
        n = 0

if n:
    k = 0
    for m in matrix:
        for i in range(k + 1):
            if m[i] != 0 and i != k:
                zmatrix.append(zerodation(matrix, m, k, len(m)))
            print(i)
        k += 1

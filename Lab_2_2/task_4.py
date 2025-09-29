def transpose_matrix(matrix):
    rows = 0
    for num in matrix:
        rows += 1
    cols = 0
    if rows > 0:
        for num in matrix[0]:
            cols += 1
    transposed = []
    i = 0
    while i < cols:
        new_row = []
        j = 0
        while j < rows:
            new_row.append(matrix[j][i])
            j += 1
        transposed.append(new_row)
        i += 1
    return transposed

print("Введите матрицу построчно (через пробел), пустая строка - конец:")
matrix = []
while True:
    line = input()
    if line == "":
        break
    row_str = line.split()
    row = []
    for x in row_str:
        row.append(int(x))
    matrix.append(row)
print("Исходная матрица:")
for r in matrix:
    print(r)
t = transpose_matrix(matrix)
print("Транспонированная матрица:")
for r in t:
    print(r)

import random
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))


matrix = []
scetchic = 0

if rows <=0:
    print("Число должно быть положительным")
    exit()
    if cols <= 0:
        print("Число должно быть положительным")
        exit()
    else:
        pass
else:
    pass


for _ in range(rows):
    row = []
    for _ in range(cols):
        num = random.randint(1, 10)
        row.append(num)
    matrix.append(row)
print("Сгенерированный массив:")
for row in matrix:
    print(row)

for i in range(rows):
    for j in range(cols):
       if matrix[i][j] == 5:
            scetchic += 1
            matrix[i][j] = 0


print("Измененный массив:")
for row in matrix:
    print(row)


print("\nСумма значений в каждой строке:")
for i, row in enumerate(matrix):
    print(f"Строка {i + 1}: {sum(row)}")

print("\nСумма значений в каждом столбце:")
for j in range(cols):
    column_sum = sum(matrix[i][j] for i in range(rows))
    print(f"Столбец {j + 1}: {column_sum}")


print(f"\nКоличество заменённых пятёрок: {scetchic}")



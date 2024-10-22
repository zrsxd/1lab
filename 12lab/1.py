n = int(input("Введите количество элементов массива: "))

if n <= 0:
    print("Число должно быть положительным")
    exit()
else:
    pass

arr = []
print("Введите элементы массива: ")
for _ in range(n):
    arr.append(int(input()))




max_element = max(arr)
min_element = min(arr)

dif = max_element - min_element

print("Разница между максимальным и минимальным элементами:", dif)


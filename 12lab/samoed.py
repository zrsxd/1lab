import random

n = int(input("Введите количество элементов массива: "))
arr = [random.randint(-50, 25) for _ in range(n)]

if n <= 0:
    print("Число должно быть положительным")
    exit()
else:
    pass

print("Сгенерированный массив:", arr)

max_element = max(arr)
min_element = min(arr)

difference = max_element - min_element

print("Разница между максимальным и минимальным элементами:", difference)

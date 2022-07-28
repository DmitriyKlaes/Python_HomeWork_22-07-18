# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

list_1 = list(map(int, input('Задайте последовательность чисел через пробел: ').split()))
list_2 = [list_1[i] for i in range(len(list_1)) if list_1[i] not in list_1[:i]]
print(list_2)

# От препода

list_1 = [45, -10, 23, 2, 45, -10, 1]
d = {}
for i in list_1:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
arr = []
for i in d:
    if d[i] == 1:
        arr.append(i)
print(arr)

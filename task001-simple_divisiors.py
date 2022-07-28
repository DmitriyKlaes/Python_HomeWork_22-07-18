# Задайте натуральное число N. Напишите программу,
# которая составит список простых делителей числа N. (1 - составное число)

def correct_value():  # Позволяет ввести в строку только числовое значение
    result = input('Введите целое положительное число: ')
    while not result.isdigit() or int(result) == 0:
        result = input('Неверный ввод! Введите целое число > 0: ')
    return int(result)


def simple_divisiors(number):
    devisior = 2
    result_list = []
    while number > 1:
        if not number % devisior:
            result_list.append(devisior)
            number //= devisior
        else:
            devisior += 1
    return result_list


print(simple_divisiors(correct_value()))

# От препода

n = int(input())
for i in range(2, n + 1):
    if n % i == 0:
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
            if count > 2:
                break
        if count == 2:
            print(i, end=' ')

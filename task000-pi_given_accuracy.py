# Вычислить число c заданной точностью d
# Пример:
# - при d = 3, π = 3.141

def correct_value():  # Позволяет ввести в строку только числовое значение
    result = input('Введите колличество значений после запятой в числе Pi: ')
    while not result.isdigit() or int(result) == 0:
        result = input('Неверный ввод! Введите целое число > 0: ')
    return int(result)

def pi(): # функция для вычисления числа ПИ по формуле Лейбница
    denominator, sum = 1, 0
    for i in range(1000000):
        if i % 2 == 0:
            sum += 4 / denominator
        else:
            sum -= 4 / denominator
        denominator += 2
    return sum

accuracy = lambda x, y: int(x * 10 ** y) / 10 ** y 
result = accuracy(pi(), correct_value())
print(pi())
print(result)

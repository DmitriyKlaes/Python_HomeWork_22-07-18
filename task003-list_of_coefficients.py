# Задана натуральная степень k.
# Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и вывести на экран.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# Вариант решения с использованием модуля с итераторами:

from random import randint
import itertools


def hard_polynomial(k, coefficient):
    x = ['*x^'] * (k - 1) + ['*x']
    polynomial = [[a, b, c] for a, b, c in itertools.zip_longest(coefficient, x, range(k, 1, -1), fillvalue='')]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    polynomial.insert(0, ' ')
    return "".join(map(str, polynomial)).replace(' 1*x', ' x').replace(' 0*x', ' x')


k = int(input('Введите натуральную степень многочлена: '))
coefficient = [randint(0, 100) for i in range(k + 1)]
polynomial_1 = hard_polynomial(k, coefficient)
print(polynomial_1)


# Более простой вариант решения задачи:

def simple_polynomial(k):
    result = ' '
    while k >= 0:
        if k > 1:
            result = result + str(randint(0, 100)) + '*x^' + str(k)
        if k == 1:
            result = result + str(randint(0, 100)) + '*x'
        if k == 0:
            result = result + str(randint(0, 100)) + ' = 0'
        if k > 0:
            result = result + ' + '
        k -= 1
    return result.replace(' 1*x', ' x').replace(' 0*x', ' x')


polynomial_2 = simple_polynomial(k)
print(polynomial_2)


# От препода 1

k = int(input('Задайте натуральную степень k: '))
arr = []
for i in range(k, 0, -1):
    print(f'{rd(0, 100)}x^{i}+', end='')
print(rd(-100, 100), end='')


# От препода 2

k = int(input('Задайте натуральную степень k: '))
arr = []
for i in range(k, 0, -1):
    x = rd(-100, 100)
    if x > 0:
        print(f'+{x}x^{i}', end='')
    else:
        print(f'{x}x^{i}', end='')
print(rd(-100, 100), end='')

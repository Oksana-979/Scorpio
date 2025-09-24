from math import sqrt

a = int(input('Введите 1 сторону треугольника: '))
b = int(input('Введите 2 сторону треугольника: '))
c = int(input('Введите 3 сторону треугольника: '))
per = a + b + c
p = per / 2
# area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
area = sqrt(p * (p - a) * (p - b) * (p - c))

print(f'Площадь равна {area} периметр равен {per}')

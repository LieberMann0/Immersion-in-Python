# Напишите программу, которая вычисляет площадь круга и длину окружности по введённому диаметру.
# Диаметр не превышает 1000 у.е.
# Точность вычислений должна составлять не менее 42 знаков.

import decimal
import math

MIN_LIMIT = 1
MAX_LIMIT = 1000
PI = decimal.Decimal(math.pi)
diameter = decimal.Decimal(input(f"Введите диаметр от {MIN_LIMIT} до {MAX_LIMIT} - "))


while diameter < 1 or diameter > 1000:
    print()
    print(f"Введите диаметр ПРАВИЛЬНО! (от {MIN_LIMIT} до {MAX_LIMIT})")
    diameter = decimal.Decimal(input("Введите диаметр - "))

decimal.getcontext().prec=42

circle_area = PI * (diameter / 2) ** 2
print(circle_area)

circumference_length = PI * diameter
print(circumference_length)

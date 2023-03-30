# Создайте функцию генератор чисел Фибоначчи.

num = int(input("Введите желаемое количество цифр: - "))

def fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        yield a
        a, b = b, a + b

print(list(fibonacci(num)))

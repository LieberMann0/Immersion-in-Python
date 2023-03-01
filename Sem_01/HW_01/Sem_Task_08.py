# Нарисовать в консоли ёлку спросив у пользователя количество рядов.

MIN_ROWS = 1
MAX_ROWS = 30
number_of_rows = 0
a = 1

while number_of_rows < 1 or number_of_rows > 30:
    number_of_rows = int(input(f"Елочка в высоту может быть от {MIN_ROWS} до {MAX_ROWS} рядов.\nСколько рядов будет в вашей елочке? - "))

while number_of_rows > 0:
    print(f" " * (number_of_rows) + "*" * (a))
    number_of_rows -= 1
    a += 2

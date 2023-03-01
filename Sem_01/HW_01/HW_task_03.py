# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
#       from random import randint
#       num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
try_number = 1
try_limit = 10
num = randint(LOWER_LIMIT, UPPER_LIMIT)

print("Отгадайте число от 0 до 1000 за 10 попыток")

while try_number < (try_limit + 1):    
    attempt = int(input(f"Попытка {try_number}. Ваше число - "))
    if attempt > num:
        print("Меньше")
        try_number += 1
    elif attempt < num:
        print("Больше")
        try_number += 1
    elif attempt == num:
        print("Вы отгадали!")
        break
print("Игра окончена")




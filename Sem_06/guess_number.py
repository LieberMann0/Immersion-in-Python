# Создать модуль с функцией внутри. Функция принимает на вход три целых числа:
# нижнюю и верхнюю границы и количество попыток. Внутри генерируется случайное
# число в указанных границах и пользователь должен угадать его за азданное
# число попыток. Функция выводит подсказки "больше", "меньше".
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.


from random import randint


def guess(down:int, up:int, chanse:int) -> bool:
    number = randint(down, up)

    for i in range(chanse):
        print(f"Enter number from {down} to {up} ")
        num = int(input())
        if num > number:
            print(" Number is smaller ")
        elif num < number:
            print(" Number is bigger ")
        else:
            return True
    return False


if __name__ == '__main__':

    down = int(input('Enter first number: '))
    up = int(input('Enter second number: '))
    chanse = int(input('Enter third number: '))
    print(guess(down, up, chanse))


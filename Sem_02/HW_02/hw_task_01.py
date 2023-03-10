# Напишите программу, которая получает целое число и возвращает
# его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

number = int(input("Введите число: - "))
print()
HEX_CALC = 16
result = ""

print(hex(number))
print()

while number > 0:    
    remainder = number % HEX_CALC
    match remainder:
        case 10:
            result = "a" + result
        case 11:
            result = "b" + result
        case 12:
            result = "c" + result        
        case 13:
            result = "d" + result
        case 14:
            result = "e" + result
        case 15:
            result = "f" + result
        case _:
            result = str(remainder) + result    
    number = number // HEX_CALC
print(result)

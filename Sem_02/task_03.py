# Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.

# Функции bin и oct используйте для проверки своего
# результата, а не для решения.

# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
#    в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно


number: int = int(input("Введите число: - "))
print()
BIN_CALC = 2
OCT_CALC = 8

print(bin(number))
print(oct(number))
print()

for i in BIN_CALC, OCT_CALC:
    a: int = number
    result: str = ""
    while a > 0:    
        remainder: int = a % i
        result: str = str(remainder) + result
        a: int = a // i
    print(result)
    
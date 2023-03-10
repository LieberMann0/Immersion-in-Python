# Напишите программу, которая принимает две строки
# вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.


import fractions

fract1 = str(input("Введите первую дробь в виде a/b - "))
a = int(fract1[0])
b = int(fract1[2])
fist_fr = fractions.Fraction(a, b)

fract2 = str(input("Введите вторую дробь в виде a/b - "))
a2 = int(fract2[0])
b2 = int(fract2[2])
second_fr = fractions.Fraction(a2, b2)

print()

fract_sum = (a * b2 + a2 * b) / b * b2
fract_mult = a * a2 / b * b2

print("Сумма  ", (a * b2 + a2 * b), "/", (b * b2), end=" -> ")
print(fist_fr + second_fr)
print("Произведение  ", (a * a2), "/", (b * b2), end=" -> ")
print(fist_fr * second_fr)

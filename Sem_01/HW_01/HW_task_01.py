# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого
# отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше
# суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

a = int(input("Сторона А - "))
b = int(input("Сторона B - "))
c = int(input("Сторона C - "))

if (a + b) < c or (b + c) < a or (a + c) < b:
    print("Треугольник не существует")
else:
    if (a == b and b != c) or (b == c and c != a) or (c == a and a != b):
        print("Треугольник равнобедренный")
    elif a == b and b == c and c == a:
        print("Треугольник равносторонний")
    else:
        print("Треугольник разносторонний")

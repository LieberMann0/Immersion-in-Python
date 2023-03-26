# Функция получает на вход строку из двух чисел через пробел.
# Сформируйте словарь, где ключом будет символ из Unicode, а значением — целое число.
# Диапазон пар ключ-значение от наименьшего из введённых пользователем
# чисел до наибольшего включительно.

def double_num(n: str) -> dict[str, int]:
    one, two = map(int, n.split())
    result = {}

    for i in range(min(one, two), max(one, two) + 1):
        result[chr(i)] = i

    return result

print(double_num("1 5"))

# Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# Строки нумеруются начиная с единицы.
# Слова выводятся отсортированными согласно кодировки Unicode.
# Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.



def words_of_string(my_string: str) -> None:
    """First decision."""
    sorted_string = sorted(my_string.split())
    count = 0

    for i in sorted_string:
        if len(i) > count:
            count = len(i)

    for i, j in enumerate(sorted_string, start=1):
        print(f"{i} {j:>{count}}")

words_of_string(input("Введите строку: - "))


def words_of_string_2(my_string: str) -> None:
    """Second decision."""
    sorted_string = sorted(my_string.split())
    max_len = len(max(sorted_string, key=len))    

    for i, j in enumerate(sorted_string, start=1):
        print(f"{i} {j:>{max_len}}")

words_of_string_2(input("Введите строку: - "))

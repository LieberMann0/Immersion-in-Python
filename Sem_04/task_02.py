# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

def char_to_code(text: str) -> list[int]:
    result = set()

    for i in text:
        result.add(ord(i))
    result = sorted(result, reverse=True)
    return result

print(char_to_code(input("Введите строку: - ")))



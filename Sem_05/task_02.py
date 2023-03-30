# Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.


my_string = "Моя строка"
my_dict = {key: ord(key) for key in my_string}
print(my_dict)


"""Другой вариант"""
other_dict = {}
for key in my_string:
    other_dict[key] = ord(key)

print(other_dict)

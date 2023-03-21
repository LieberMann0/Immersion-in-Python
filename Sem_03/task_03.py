# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
#       ключ — тип элемента,
#       значение — список элементов данного типа.

my_tuple = (123, "Egg", 111, False, 1.23, 9999, 12.3, True, "Spam", 3.14)
my_dict = {}

for i in my_tuple:
    key = my_dict.setdefault(type(i), list())
    key.append(i)

print(my_dict)

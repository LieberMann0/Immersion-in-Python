# Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.

my_list = [1, 0, 4, 9, 5, 7, 0, 5, 0, 8, 1, 3, 9, 3, 4, 8, 8, 1, 9, 7, 5, 6, 9, 1, 3, 9, 5, 2]

for i in set(my_list):
    if my_list.count(i) > 1:
        for item in range(my_list.count(i)):
            my_list.remove(i)

print(my_list)

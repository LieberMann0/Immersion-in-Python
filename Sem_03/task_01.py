#   Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.
#
#   *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.

different_num = [1, 2, 4, 1, 4, 9, 8, 7, 6, 5, 9, 4, 0, 1, 8, 4, 2, 3, 8, 9, 4, 7]
unique_num = []

for elem in different_num:
    if elem not in unique_num:
        unique_num.append(elem)

print(unique_num)


#Второе решение

unique_num2 = list(set(different_num))
print(unique_num2)

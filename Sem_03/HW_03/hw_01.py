#     Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.


my_list = [1, 0, 4, 9, 5, 7, 0, 5, 0, 8, 1, 3, 9, 4, 1, 9, 5, 6, 9, 1, 9, 5, 2]
double_elements_list = []

for i in my_list:
    x = my_list.count(i)    
    if x > 1:
        if i not in double_elements_list:            
            double_elements_list.append(i)        

print(double_elements_list)

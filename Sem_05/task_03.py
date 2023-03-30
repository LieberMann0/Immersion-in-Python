# Возьмите словарь, сохраните его итераторатор.
# Далее выведите первые 5 пар ключ-значение,обращаясь к итератору, а не к словарю.


my_string = "Моя строка"
my_dict = {key: ord(key) for key in my_string}
my_iter = iter(my_dict.items())
for i in range(5):
    print(next(my_iter))

# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента,
# а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


def swap_places_in_dictionary(**parameters):
    for key, value in parameters.items():            
        print(value, key)
        

my_dict = {"Маша": 5, "Петя": 4, "Клава": 3, "Вовочка": 2}
print(swap_places_in_dictionary(**my_dict))





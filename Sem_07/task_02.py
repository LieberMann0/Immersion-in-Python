# Напишите функцию, которая генерирует
# псевдоимена.
#  Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
#  Полученные имена сохраните в файл.

from random import randint


glas_str = ['a', 'e', 'i', 'o', 'u']
sogl_str = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

def func(cnt_line:int, file_name:str):
    with open(file_name, 'w', encoding='utf-8') as f:
        for _ in range(cnt_line):
            result_str = ""
            for _ in range(randint(2, 4)):
                result_str += glas_str[randint(0, len(glas_str)-1)] \
                        + sogl_str[randint(0, len(sogl_str)-1)]

                result_str = result_str.capitalize()

                print(result_str)
                f.write(f'{result_str}\n')

if __name__ == '__main__':
    func(5, "data.txt")



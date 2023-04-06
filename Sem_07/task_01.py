# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
#  Первое число int, второе - float разделены вертикальной чертой.
#  Минимальное число - -1000, максимальное - +1000.
#  Количество строк и имя файла передаются как аргументы функции

from random import randint, uniform


MIN_LIMIT = -1000
MAX_LIMIT = 1000


def func(cnt_line: int, file_name: str) -> None:
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(cnt_line):           
            f.write(f"{randint(MIN_LIMIT, MAX_LIMIT)} | {uniform(MIN_LIMIT, MAX_LIMIT)}\n")


if __name__ == '__main__':
    func(5)

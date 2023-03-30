# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх элементов:
#   путь, имя файла, расширение файла.


my_string = "C:/Users/Администратор/Desktop/my_text.txt"

def three_of_path(s):
    path, f = s.rsplit("/", 1)
    f_name, ext = f.split('.')
    return (path, f_name, ext)

print(three_of_path(my_string))

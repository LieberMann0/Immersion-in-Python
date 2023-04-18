# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)

from time import time
from time import ctime


class MyString(str):
    """Class str"""

    def __new__(cls, value: str, author: str):
        """create new instance"""
        instance = super().__new__(cls, value)
        instance.author = author.capitalize()
        instance.time = ctime(time())
        return instance


if __name__ == '__main__':
    s1 = MyString('some text', 'Mike')
    print(s1)
    print(s1.author)
    print(s1.time)
    help(MyString)

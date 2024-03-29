# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.


class Rectangle:

    def __init__(self, side_a: float, side_b=None):
        if side_a <= 0:
            raise ValueError(f'value must be greater than 0')
        else:
            self.side_a = side_a
            if side_b is None:
                self.side_b = side_a
            elif side_b <= 0:
                raise ValueError(f'value must be greater than 0')
            else:
                self.side_b = side_b


    def square_rectangle(self):
        return self.side_a * self.side_b
        

    def len_rectangle(self):
        return (self.side_a + self.side_b) * 2


if __name__ == '__main__':
    rect = Rectangle(5, -10)
    print(rect.len_rectangle(), rect.square_rectangle())

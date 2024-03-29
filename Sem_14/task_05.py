# На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину,
# а также вычисляющую периметр, площадь и позволяющий складывать и вычитать
# прямоугольники беря за основу периметр.
# Напишите 3-7 тестов unittest для данного класса.

import unittest


class Rectangle:

    def __init__(self, side_a: float, side_b=None):
        self.side_a = side_a
        if side_b is None:
            self.side_b = side_a
        else:
            self.side_b = side_b


    def square_rectangle(self):
        return self.side_a * self.side_b


    def len_rectangle(self):
        return (self.side_a + self.side_b) * 2


class TestCaseName(unittest.TestCase):
    def setUp(self) -> None:
        self.r1 = Rectangle(5, 15)
        self.r2 = Rectangle(5, 5)
        self.r3 = Rectangle(5, 10)


    def test_sqare(self):
        self.assertEqual(self.r1.square_rectangle(), 75)
        

    def test_len(self):
        self.assertEqual(self.r1.len_rectangle(), 40)


if __name__ == '__main__':
    unittest.main(verbosity=2)

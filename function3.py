import unittest
from function_number_2 import function_2

class TestFunction2(unittest.TestCase):   #создаем класс для проделывания тестов

    def test_1(self):
        "Тест 1: Обычные целые положительные числа(удовлетворяющие всем условиям)"
        self.assertEqual(function_2(5, 3, 6, 2, 4), 4)  #assertEqual проверяет равенство чисел

    def test_2(self):
        "Тест 2: Проверка деления на ноль (c == d)"
        self.assertIsNone(function_2(1, 1, 2, 2, 9))

    def test_case_3_negative_root(self):
        "Тест 3: Проверка корня отрицательного числа (f < 0)"
        self.assertIsNone(function_2(1, 1, 5, 2, -4))

    def test_case_4_negative_numbers(self):
        "Тест 4: Разность отрицательных чисел и корень 0"
        self.assertEqual(function_2(-2, -4, -1, -3, 0), -3.0)

    def test_case_5_float_numbers(self):
        "Тест 5: Работа с дробными числами (float)"
        self.assertEqual(function_2(1.5, 2.5, 5.0, 3.0, 0.25), 2.5)


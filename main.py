import unittest
from function_1 import function as function_base
from function_2 import function_number_2
from function3 import TestFunction2


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFunction2) #хранит в себе все тесты
    runner = unittest.TextTestRunner(verbosity=2)  #запускает тесты,verbosity-показывает название каждого теста
    runner.run(suite) #запускаем тесты и выводим результаты
    print("демонстрация работы функций\n")
    cases = [("Позитивный тест", (5, 3, 6, 2, 4)),("Деление на ноль ", (1, 1, 2, 2, 9)),("Отрицательный корень", (1, 1, 5, 2, -4)),]#создали список кортежей,
                                                                                                                                     #т.е. заранее прописали наборы данных,подающихся на тесты
    for name, args in cases: #перебираем все тесты,попутно разделяя названия тестов и поданные значение(кортежи)
        print(f"Данные: {args} ({name})")#выводим входные данные и имя теста
        print(" Функция_2 (с проверками): ", end="") #вывод результата(end помогает не переносить курсос на следующую строку)
        print(function_number_2(*args))
        print("  Функция_1 (без проверок): ", end="")
        try: #отловщик ошибок
            print(function_base(*args)) #вызываем функцию 1 с заданными аргументами
        except (ZeroDivisionError, ValueError) as error: #ошибка деления на 0 или отрицательного числа под корнем
            print(f"Ошибка падения функции :{type(error).__name__}") #выводим название ошибки
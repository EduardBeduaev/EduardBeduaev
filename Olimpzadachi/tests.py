from unittest import TestCase, main
from main import func


class TestMain(TestCase):
    def setUp(self):
        self.poisk = func

    def test_maxel_potom_ydakenie(self):
        a = [1, 2, 3, 4, 5, 6, 7, 21]
        self.assertEqual(self.poisk(a), 7)

    def test_if_not_all_int(self):
        a = [1, 2, 3, 4, "1", "5"]
        with self.assertRaises(ValueError):
            self.assertEqual(self.poisk(a), 5)

# class TestMain(TestCase):
#     def setUp(self):
#         self.func_sum = f
#
#
#     def test_f_if_ab_natural_numbers(self):
#         self.assertEqual(self.func_sum(5,6), 11)
#

# ОПЦИОНАЛАЬНО: содержат слово test в названии
# ПОДРОБНО ОПИСЫВАЮТ МЕСТО ТЕСТИРОВАНИЯ
# *обязательно типизировано всё
# сначала ошибочный тест

import unittest
from dz8_function import * # calculate, measure_time


class TestCalculate(unittest.TestCase):
    def test_calculate(self):
        expected = sum(range(10 * 10 ** 6))
        actual = calculate()
        self.assertEqual(actual, expected)


class TestMeasureTime(unittest.TestCase):
    def test_measure_time_returns_result(self):
        def test_function():
            return 123
        result = measure_time(test_function)
        self.assertEqual(result, 123)

if __name__ == "__main__":
    unittest.main()
import unittest

from codetest import checkNumber


class CheckNumberTest(unittest.TestCase):
    def test_plain_numbers(self):
        self.assertEqual(checkNumber(1), "1")
        self.assertEqual(checkNumber(2), "2")

    def test_single_divisors(self):
        self.assertEqual(checkNumber(3), "Fizz")
        self.assertEqual(checkNumber(5), "Buzz")
        self.assertEqual(checkNumber(7), "Fool")
        self.assertEqual(checkNumber(9), "Fizz")

    def test_combined_divisors(self):
        self.assertEqual(checkNumber(15), "FizzBuzz")
        self.assertEqual(checkNumber(70), "BuzzFool")
        self.assertEqual(checkNumber(105), "FizzBuzzFool")


if __name__ == "__main__":
    unittest.main()

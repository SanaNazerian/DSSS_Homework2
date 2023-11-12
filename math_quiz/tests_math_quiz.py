import unittest
from math_quiz import generate_rand_integer, generate_rand_operator, math_operation


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num =generate_rand_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        operator = ['+', '-', '*']
        for _ in range(1000):
             rand_op = generate_rand_operator()
             self.assertIn(rand_op, operator)
             self.assertIsInstance(rand_op, str)

    def test_function_C(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 3, '-', '8 - 3', 5),
            (4, 6, '*', '4 * 6', 24),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = math_operation(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
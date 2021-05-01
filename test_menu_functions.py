import unittest
from menu_functions import split

animals_list_1 = ['monkey', 'racoon', 'bear', 'roe']


class MethodsTestCase(unittest.TestCase):

    def test_split(self):
        # a few tests for a split function
        self.assertEqual(split('monkey, racoon, bear, roe'), animals_list_1)
        self.assertEqual(split('monkey, racoon121212, bear, roe'), ['monkey', 'racoon121212', 'bear', 'roe'])
        self.assertEqual(split('monkey,dfdfdfdffd racoon, bear, roe'), ['monkey', 'dfdfdfdffdracoon', 'bear', 'roe'])
        self.assertEqual(split('15, 123, 1, 22'), ['15', '123', '1', '22'])


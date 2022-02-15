from latex_table_generator import check_dimension
from pymonad.maybe import Just, Nothing
import unittest


class TestTableGenerator(unittest.TestCase):
    def test_check_dimension(self):
        self.assertEqual(check_dimension([['a'], ['b']]), Just([['a'], ['b']]))
        self.assertEqual(check_dimension([['a', 'b', 'c'], ['a', 'b', 'c']]), Just([['a', 'b', 'c'], ['a', 'b', 'c']]))
        self.assertEqual(check_dimension([['a'], ['b', 'c']]), Nothing)
        self.assertEqual(check_dimension([]), Nothing)
        self.assertEqual(check_dimension([[]]), Nothing)

    def test_create_table(self):
        pass
        # self.assertEqual([a])


if __name__ == '__main__':
    unittest.main()

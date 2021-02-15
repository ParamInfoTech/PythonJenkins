import unittest2
import mycalc

class TestClass(unittest2.TestCase):

    def test_add(self):
        self.assertEqual(mycalc.add(10, 5), 15)
        self.assertEqual(mycalc.add(10, 1), 11)

    def test_subtract(self):
        self.assertEqual(mycalc.subtract(10, 5), 5)

    def test_divide(self):
        self.assertEqual(mycalc.divide(10, 2), 5)
        with self.assertRaises(ValueError):
            mycalc.divide(10, 0)

if __name__ == "__main__":
    unittest2.main()


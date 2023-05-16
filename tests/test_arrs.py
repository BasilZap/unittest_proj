import unittest
from utils import arrs
from utils.arrs import get
from utils.arrs import my_slice


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([1, 2, 3], -1, "test"), "test")
        self.assertEqual(arrs.get([1, 2, 3], -1), None)

    def test_get__empty_list(self):
        with self.assertRaises(IndexError):
            get([], 0)
            get([], 1)

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 0, 0), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], 0, 1), [1])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], -2, -1), [4])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], 2, -1), [3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], -2), [4, 5])
        self.assertEqual(arrs.my_slice([], 1, -1), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -6), [1, 2, 3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], 0, -7), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], 0, 7), [1, 2, 3, 4, 5])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], 1, 0), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], -1, 2), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], 10, 2), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], 10, 10), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], -10, -10), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], 1, None), [2, 3, 4, 5])

    def test_get__test_slice(self):
        with self.assertRaises(TypeError):
            my_slice([1, 2, 3], None, None)

#!/usr/bin/python3
"""Unittest for the max_integer module
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestMaxInteger
    Args:
        unittest (lsit): Unit test case for max_integer module
    """

    def test_regular_list(self):
        """Test with a list of integers and should return the max result"""
        sample_list = [1, 2, 3, 4, 5]
        result = max_integer(sample_list)
        self.assertEqual(result, 5)

    def test_not_int(self):
        """Test with a list of elements including
        non-integers and integers:
        should raise a TypeError exception"""
        sample_list = ["a", "b", 9]
        self.assertRaises(TypeError, max_integer, sample_list)

    def test_empty(self):
        """Test with an empty list: should return None"""
        sample_list = []
        result = max_integer(sample_list)
        self.assertEqual(result, None)

    def test_negative(self):
        """Test with a list of negative integers: should return the max"""
        sample_list = [-2, -6, -1]
        result = max_integer(sample_list)
        self.assertEqual(result, -1)

    def test_float(self):
        """Test with a list of mixed ints and floats: should return the max"""
        sample_list = [3, 4.5, 2]
        result = max_integer(sample_list)
        self.assertEqual(result, 4.5)

    def test_not_list(self):
        """Test with a parameter that's not a list: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, 7)

    def test_unique(self):
        """Test with a list of one int: should return the value of this int"""
        sample_list = [45]
        result = max_integer(sample_list)
        self.assertEqual(result, 45)

    def test_identical(self):
        """Test with a list of identical values: should return the value"""
        sample_list = [8, 8, 8, 8, 8]
        result = max_integer(sample_list)
        self.assertEqual(result, 8)

    def test_strings(self):
        """Test with a list of strings: should return the first string"""
        sample_list = ["hi", "hello"]
        result = max_integer(sample_list)
        self.assertEqual(result, "hi")

    def test_none(self):
        """Test with a None as parameter: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, None)

    def test_higher_list_dimensions(self):
        """First dimension list members can themselves also be iterables
        (except sets, as they always return <list>[0].) Those iterables
        can be of varying length in the same dimension, but must all be
        of the same dimensional depth to avoid a TypeError in comparison.
        For comparison of any values in elements with dimensions beyond
        the first, it will always be the first value to be compared by
        the program: <list>[i][0][0]..., <list>[i + 1][0][0]..., ...
        """

        self.assertEqual(max_integer([[5, 4, 1], [6, 3], []]), [6, 3])
        self.assertEqual(max_integer([(5, 4, 1), (6, 3), ()]), (6, 3))
        self.assertEqual(max_integer(['azzz', 'byy', 'cx']), 'cx')
        self.assertEqual(max_integer([[[1, 2], [2], []], [[4], [5]], [[6]]]),
                         [[6]])
        self.assertEqual(max_integer([[[8, 2], [2], []], [[4], [5]], [[6]]]),
                         [[8, 2], [2], []])
        self.assertEqual(max_integer([{5, 4}, {6, 3, 1}, {20}]), {4, 5})


if __name__ == '__main__':
    unittest.main()

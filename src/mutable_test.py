# -*- coding: utf-8 -*-
"""
# @Author: Wzx
# @Date: 2021/3/24 18:21
# @File: mutable_test.py
# @Software: PyCharm
# @Description: 

"""
import unittest
from hypothesis import given
import hypothesis.strategies as st
from mutable import *


class TestMutableDict(unittest.TestCase):

    def test_add(self):
        dict = MyDict()
        dict.add(1, 2)
        dict.add(2, 2)
        dict.add('0', 2)
        self.assertEqual(dict.to_list(), [[1, 2], [2, 2], ['0', 2]])

    def test_remove(self):
        dict = MyDict()
        dict.add(1, 2)
        dict.add(2, 2)
        dict.add('0', 2)
        dict.remove(2)
        self.assertEqual(dict.to_list(), [[1, 2], ['0', 2]])
        try:
            dict.remove(3)
        except AttributeError as error:
            self.assertEqual(error.args[0], "The element does not exist")

    def test_size(self):
        dict = MyDict()
        dict.add(1, 2)
        dict.add(2, 2)
        dict.add('0', 2)
        self.assertEqual(dict.size(), 3)

    def test_Conversion(self):
        dict = MyDict()
        dict.from_list([[0, 1], [2, 1], [3, 1]])
        self.assertEqual(dict.to_list(), [[0, 1], [2, 1], [3, 1]])

    def test_find_key(self):
        dict = MyDict()
        dict.add(1, 1)
        dict.add(2, 3)
        dict.add('0', 2)
        self.assertEqual(dict.find_key(1), 1)

    def test_iterator(self):
        dict = MyDict()
        dict.add(1, 2)
        dict.add(2, 2)
        dict.add('0', 2)
        list = dict.to_list()
        iter = dict.__iter__()
        test = []
        while iter.has_next():
            test.append(iter.__next__())
        self.assertEqual(test, list)
        self.assertRaises(StopIteration, lambda: iter.__next__())

    def test_filter(self):
        def func(k):
            if k % 2 == 0:
                return True
            return False

        dict = MyDict()
        dict.add(1, 2)
        dict.add(2, 2)
        dict.add('0', 2)
        list = dict.to_list()
        list2 = []
        for i in range(len(list)):
            if type(list[i][0]) is str:
                if func(ord(list[i][0])):
                    list2.append(list[i])
            else:
                if func(list[i][0]):
                    list2.append(list[i])
        itor = dict.filter(func)
        test = []
        while itor.has_next():
            test.append(itor.__next__())
        self.assertEqual(test, list2)

    def test_map(self):
        def func(k):
            k + 1

        dict = MyDict()
        dict.add(1, 2)
        dict.add(2, 2)
        dict.add('0', 2)
        list = dict.to_list()
        list2 = []
        for i in list:
            i[1] = func(i[1])
            list2.append(i)

        iter = dict.map(func)
        test = []
        while iter.has_next():
            test.append(iter.__next__())
        self.assertEqual(test, list2)

    def test_reduce(self):
        def func(k, j):
            return k + j

        dict = MyDict()
        dict.add(1, 2)
        dict.add(2, 2)
        dict.add('0', 2)
        sum = dict.reduce(func)
        self.assertEqual(sum, 6)

    def test_dict(self):
        dict = MyDict()
        self.assertEqual(dict.getting(1), None)
        dict.setting(0, 1)
        self.assertEqual(dict.getting(0), 1)
        dict.setting(0, 2)
        self.assertEqual(dict.getting(0), 2)
        dict.setting(1, None)
        self.assertEqual(dict.getting(1), None)

    def test_mconcat(self):
        dict1 = MyDict()
        dict2 = MyDict()
        dict3 = MyDict()
        dict1.setting(1, 1)
        dict1.add(1, 2)
        dict1.add(2, 2)
        dict1.add(0, 2)
        dict2.setting(-1, 1)
        dict2.add(-1, 2)
        dict2.add(3, 2)
        dict2.add('1', 3)
        dict3.mconcat(dict1, dict2)
        self.assertEqual(dict3.to_list(), [[-1, 2], [0, 2], [1, 2], [2, 2], [3, 2], ['1', 3]])
        dict3.mconcat(dict2, dict1)
        self.assertEqual(dict3.to_list(), [[-1, 2], [0, 2], [1, 2], [2, 2], [3, 2], ['1', 3]])

    @given(st.lists(st.lists(st.integers(), min_size=2, max_size=2), max_size=1))
    def test_from_list_to_list_equality(self, a):
        # The generated test data is processed
        dict = MyDict()
        dict.from_list(a)
        self.assertEqual(dict.to_list(), a)

    @given(st.lists(st.lists(st.integers(), min_size=2, max_size=2), max_size=1))
    def test_monoid_identity(self, test_List):
        # The generated test data is processed
        dict1 = MyDict()
        dict2 = MyDict()
        dict3 = MyDict()
        dict1.from_list(test_List)
        b = dict1.mempty()
        dict2.mconcat(dict1, b)
        self.assertEqual(dict1.to_list(), dict2.to_list())
        self.assertEqual(dict2.to_list(), dict1.to_list())
        dict3.mconcat(b, dict1)
        self.assertEqual(dict2.to_list(), dict3.to_list())
if __name__ == "__main__":
    unittest.main()

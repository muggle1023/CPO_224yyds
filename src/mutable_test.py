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
from src.mutable_dict import *


class TestMutableList(unittest.TestCase):

    def test_add(self):
        dict = M_dict()
        dict.add(1, 2)
        dict.add(2, 2)
        dict.add(0, 2)
        self.assertEqual(dict.tolist(), [[0, 2], [1, 2], [2, 2]])

    def test_remove(self):
        dict = M_dict()
        dict.add(1, 2)
        dict.add(2, 2)
        dict.add(0, 2)

        dict.remove(1)
        self.assertEqual(dict.tolist(), [[0, 2], [2, 2]])

    def test_size(self):
        dict = M_dict()
        dict.add(1, 2)
        dict.add(2, 2)
        dict.add(0, 2)
        self.assertEqual(dict.size(), 3)

    def test_Conversion(self):
        dict = M_dict()
        dict.fromlist([[0, 1], [2, 1], [3, 1]])
        self.assertEqual(dict.tolist(), [[0, 1], [2, 1], [3, 1]])

    def test_find(self):
        dict = M_dict()
        dict.add(1, 2)
        dict.add(2, 2)
        dict.add(0, 2)
        self.assertEqual(dict.find(2), 2)

    def test_iterator(self):
        dict = M_dict()
        dict.add(1, 2)
        dict.add(2, 2)
        dict.add(0, 2)
        list = dict.tolist()
        itor = dict.iterator()
        test = []
        while itor.has_next():
            test.append(itor.next())
        self.assertEqual(test, list)
        self.assertRaises(StopIteration, lambda: itor.next())

    def test_filter(self):
        def func(k):
            if k % 2 == 0:
                return True
            return False

        dict = M_dict()
        dict.add(1, 2)
        dict.add(2, 2)
        dict.add(0, 2)
        list = dict.tolist()
        list2 = []
        for i in range(len(list)):
            if func(list[i][0]):
                list2.append(list[i])

        itor = dict.filter(func)
        test = []
        while itor.has_next():
            test.append(itor.next())
        self.assertEqual(test, list2)

    def test_map(self):
        def func(k):
            k + 1

        dict = M_dict()
        dict.add(1, 2)
        dict.add(2, 2)
        dict.add(0, 2)
        list = dict.tolist()
        list2 = []
        for i in list:
            i[1] = func(i[1])
            list2.append(i)

        itor = dict.map(func)
        test = []
        while itor.has_next():
            test.append(itor.next())
        self.assertEqual(test, list2)

    def test_reduce(self):
        def func(k, j):
            return k + j

        dict = M_dict()
        dict.add(1, 2)
        dict.add(2, 2)
        dict.add(0, 2)
        sum = dict.reduce(func)
        self.assertEqual(sum, 6)

    def test_dict(self):
        d = M_dict()
        self.assertEqual(d.getting(1), None)
        d.setting(0, 1)
        self.assertEqual(d.getting(0), 1)
        d.setting(0, 2)
        self.assertEqual(d.getting(0), 2)
        d.setting(1, None)
        self.assertEqual(d.getting(1), None)

if __name__ == "__main__":
    unittest.main()

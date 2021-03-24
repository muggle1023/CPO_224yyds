# -*- coding: utf-8 -*-
"""
# @Author: Wzx
# @Date: 2021/3/24 15:30
# @File: mutable_dict.py
# @Software: PyCharm
# @Description: implement Dictionary based on binary-tree as a mutable object

"""
from hypothesis import given
import hypothesis.strategies as st

class Node:

    def __init__(self, key, value, rchild=None, lchild=None):
        self.k = key
        self.v = value
        self.rc = rchild
        self.lc = lchild
        self.count = 0


class TreeIterator:

    def __init__(self, data):
        self.index = -1
        self.len = len(data)
        self.data = data

    def next(self):
        self.index += 1
        if self.len > self.index:
            return self.data[self.index]
        else:
            raise StopIteration

    def has_next(self):
        if self.len > self.index + 1:
            return True
        else:
            return False


class M_dict():
    count = 0
    root = None

    def getting(self, key):
        if self.count == 0:
            return None
        else:
            return self.find(key)

    def setting(self, key, value):
        if self.count == 0:
            self.root = Node(key, value)
            self.count += 1
        else:
            self.add(key, value)

    def iterator(self):
        list = self.tolist()
        list2 = []
        for i in list:
            list2.append(i)
        return TreeIterator(list2)

    def add(self, key, value):
        if self.root == None:
            self.root = Node(key, value)
            self.count += 1
            return True
        return self.addt(self.root, key, value)

    def remove(self, key):
        list = self.tolist()
        for i in range(len(list)):
            if key == list[i][0]:
                list.pop(i)
                break
        self.root = None
        self.count = 0
        self.fromlist(list)

    def size(self):
        return self.count

    def fromlist(self, list):

        if len(list) == 0:
            return None
        while len(list) != 0:
            temp = list.pop()
            self.add(temp[0], temp[1])

    def tolist(self):
        list = []

        def func(node, list):
            if node != None:
                func(node.lc, list)
                temp = []
                temp.append(node.k)
                temp.append(node.v)
                list.append(temp)

                func(node.rc, list)

        func(self.root, list)
        return list

    def find(self, key):
        return self.findt(self.root, key)

    def addt(self, n, key, value):
        if key == n.k:
            n.v = value
            return True
        if key < n.k:
            if n.lc == None:
                n.lc = Node(key, value)
                self.count += 1
                return True
            else:
                return self.addt(n.lc, key, value)
        if key > n.k:
            if n.rc == None:
                n.rc = Node(key, value)
                self.count += 1
                return True
            else:
                return self.addt(n.rc, key, value)

    def findt(self, n, key):
        if n.k == key:
            return n.v
        if key < n.k:
            if n.lc == None:
                return None
            return self.findt(n.lc, key)
        if key > n.k:
            if n.lc == None:
                return None
            return self.findt(n.rc, key)

    def filter(self, func):
        list = self.tolist()
        list2 = []
        for i in list:
            if func(i[0]):
                list2.append(i)
        return TreeIterator(list2)

    def map(self, func):
        list = self.tolist()
        list2 = []
        for i in list:
            i[1] = func(i[1])
            list2.append(i)
        return TreeIterator(list2)

    def reduce(self, func):
        treeitor = self.iterator()
        if treeitor.has_next():
            res = treeitor.next()[1]
        while treeitor.has_next():
            res = func(res, treeitor.next()[1])
        return res



# -*- coding: utf-8 -*-
"""
# @Author: Wzx
# @Date: 2021/3/24 15:30
# @File: mutable.py
# @Software: PyCharm
# @Description: implement Dictionary based on binary-tree as a mutable object

"""


class Node:

    def __init__(self, key, value, rightChild=None, leftChild=None):
        self.k = key
        self.v = value
        self.rc = rightChild
        self.lc = leftChild
        self.count = 0


class TreeIterator:

    def __init__(self, data):
        self.index = -1
        self.len = len(data)
        self.data = data

    def __next__(self):
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


def mempty():
    return None


class MyDict:
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

    def __iter__(self):
        list = self.to_list()
        list2 = []
        for i in list:
            list2.append(i)
        return TreeIterator(list2)

    def add(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
            self.count += 1
            return True
        return self.addt(self.root, key, value)

    def addt(self, n, key, value):
        if type(key) is str:
            key_int = ord(key)
            if n.k == key_int:
                n.v = value
                return True
            if n.k > key_int:
                if n.lc is None:
                    n.lc = Node(key, value)
                    return True
                else:
                    return self.addt(n.lc, key, value)
            if n.k < key_int:
                if n.rc is None:
                    n.rc = Node(key, value)
                    return True
                else:
                    return self.addt(n.rc, key, value)
        else:
            if key == n.k:
                n.v = value
                return True
            if key < n.k:
                if n.lc is None:
                    n.lc = Node(key, value)
                    self.count += 1
                    return True
                else:
                    return self.addt(n.lc, key, value)
            if key > n.k:
                if n.rc is None:
                    n.rc = Node(key, value)
                    self.count += 1
                    return True
                else:
                    return self.addt(n.rc, key, value)

    def size(self):
        return self.count

    def from_list(self, list):
        if len(list) == 0:
            return None
        while len(list) != 0:
            temp = list.pop()
            self.add(temp[0], temp[1])

    def to_list(self):
        list = []

        def func(n, list):
            if n is not None:
                func(n.lc, list)
                temp = []
                temp.append(n.k)
                temp.append(n.v)
                list.append(temp)
                func(n.rc, list)

        func(self.root, list)
        return list

    def remove(self, key):
        list = self.to_list()
        for i in range(len(list)):
            if key == list[i][0]:
                list.pop(i)
                break
        self.root = None
        self.count = 0
        self.from_list(list)

    def find(self, key):
        return self.findt(self.root, key)

    def findt(self, n, key):
        if n.k == key:
            return n.v
        if key < n.k:
            if n.lc is None:
                return None
            return self.findt(n.lc, key)
        if key > n.k:
            if n.lc is None:
                return None
            return self.findt(n.rc, key)

    def filter(self, func):
        list = self.to_list()
        list2 = []
        for i in list:
            if func(i[0]):
                list2.append(i)
        return TreeIterator(list2)

    def map(self, func):
        list = self.to_list()
        list2 = []
        for i in list:
            i[1] = func(i[1])
            list2.append(i)
        return TreeIterator(list2)

    def reduce(self, func):
        treeitor = self.__iter__()
        if treeitor.has_next():
            res = treeitor.__next__()[1]
        while treeitor.has_next():
            res = func(res, treeitor.__next__()[1])
        return res

    def mconcat(self, dict1, dict2):
        if dict1 is not None and dict2 is not None:
            list1 = dict1.to_list()
            list2 = dict2.to_list()
        else:
            if dict1 is None and dict2 is not None:
                list1 = []
                list2 = dict2.to_list()
            if dict2 is None and dict1 is not None:
                list2 = []
                list1 = dict1.to_list()
            if dict1 is None and dict2 is None:
                list1 = []
                list2 = []

        list3 = []
        while 0 < len(list1) and 0 < len(list2):
            if list1[0][0] != list2[0][0]:
                list3.append(list1.pop(0) if list1[0][0] < list2[0][0] else list2.pop(0))
            else:
                if list1[0][1] > list2[0][1]:
                    list3.append(list2.pop(0))
                    list1.pop(0)
                else:
                    list3.append(list1.pop(0))
                    list2.pop(0)
        while len(list1) > 0:
            list3.append(list1.pop(0))
        while len(list2) > 0:
            list3.append(list2.pop(0))
        return self.from_list(list3)

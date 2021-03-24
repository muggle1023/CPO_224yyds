import unittest
from hypothesis import given
import hypothesis.strategies as st
from immutable import *

class TestImmutableList(unittest.TestCase):

    def test_add(self):
        root=node(1,1)
        add(root, 0, 1)
        add(root, 1, 2)
        add(root, 2, 3)
        self.assertEqual(to_list(root), [[0,1],[1,2],[2,3]])

    def test_size(self):
        root = node(1, 1)
        add(root, 0, 1)
        add(root, 1, 2)
        add(root, 2, 3)
        add(root, 3, 4)
        self.assertEqual(size(root), 4)

    def test_remove(self):
        root=node(1,1)
        add(root, 0, 1)
        add(root, 1, 2)
        add(root, 2, 3)
        root=remove(root,2)
        self.assertEqual(to_list(root), [[0,1],[1,2]])

    def test_conversion(self):
        root=from_list([[0,0],[2,2],[3,3]])
        self.assertEqual(to_list(root), [[0, 0], [2, 2], [3, 3]])

    def test_find(self):
        root = node(1, 1)
        add(root, 0, 1)
        add(root, 1, 2)
        add(root, 2, 3)
        self.assertEqual(find(root,0), 1)

    def test_iterator(self) :

        root = node(1, 1)
        add(root, 0, 1)
        add(root, 1, 2)
        add(root, 2, 3)
        list=to_list(root)
        itor=iterator(root)
        test=[]
        while itor.has_next():
            test.append(itor.next())
        self.assertEqual(test, list)

        self.assertRaises(StopIteration, lambda : itor.next())

    def test_filter(self):
        def func(k):
            if k%2==0:
                return True
            return False
        root = node(1, 1)
        add(root, 0, 1)
        add(root, 1, 2)
        add(root, 2, 3)
        list=to_list(root)
        list2 = []
        for i in range(len(list)):
            if func(list[i][0]):
                list2.append(list[i])

        itor=filter(root, func)
        test=[]
        while itor.has_next():
            test.append(itor.next())
        self.assertEqual(test, list2)

    def test_map(self):
        def func(k):
            k+1
        root = node(1, 1)
        add(root, 0, 1)
        add(root, 1, 2)
        add(root, 2, 3)
        list=to_list(root)
        list2 = []
        for i in list:
            i[1] = func(i[1])
            list2.append(i)

        itor=map(root, func)
        test=[]
        while itor.has_next():
            test.append(itor.next())
        self.assertEqual(test, list2)

    def test_reduce(self):
        def func(k,j):
            return k+j
        root = node(1, 1)
        add(root, 0, 1)
        add(root, 1, 2)
        add(root, 2, 3)
        sum=reduce(iterator(root), func)
        self.assertEqual(sum, 6)

    def test_dict(self):
        d=dict()
        self.assertEqual(d.getting(1), None)
        d.setting(0,1)
        self.assertEqual(d.getting(0), 1)
        d.setting(0, 2)
        self.assertEqual(d.getting(0), 2)
        d.setting(1, None)
        self.assertEqual(d.getting(1), None)

    def test_conact(self):
        t1=node(1,1)
        add(t1, 0, 0)
        add(t1, 1, 1)
        add(t1, 2, 2)
        t2 = node(-1, 1)
        add(t2, -3, -3)
        add(t2, 3, 3)

        t3=conact(t1,t2)
        self.assertEqual(to_list(t3), [[-3,-3],[-1,1],[0,0],[1,1],[2,2],[3,3]])
        t3=conact(t2,t1)
        self.assertEqual(to_list(t3), [[-3,-3],[-1,1],[0,0],[1,1],[2,2],[3,3]])

if __name__ == '__main__':
    unittest.main()

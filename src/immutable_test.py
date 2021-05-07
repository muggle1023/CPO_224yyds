import unittest
from hypothesis import given
import hypothesis.strategies as st
from immutable import *

class TestImmutableList(unittest.TestCase):

    def test_add(self):
        root=node(1,1)
        add(root, 0, 1)
        add(root, 1, 2)
        add(root, 'a', 3)
        self.assertEqual(to_list(root), [[1,2],[0,1],['a',3]])

    def test_size(self):
        self.assertEqual(size(node(1,1)), 1)
        self.assertEqual(size(node(1,1,node(0,1))), 2)
        self.assertEqual(size(node(1,1,node(0,1),node(2,2))), 3)
        self.assertEqual(size(node('a',1,node(0,1),node(2,2))), 3)

    def test_remove(self):
        root1=node(1,1,node(0,1),node('a',2))
        root1=remove(root1,'a')
        self.assertEqual(to_list(root1), [[1,1],[0,1]])
        root2=node(1,1,node(0,1),node('a',2))
        root2=remove(root2,0)
        self.assertEqual(to_list(root2), [[1,1],['a',2]])
        root3=node(1,1,node(0,1),node(2,2))
        try:remove(root3,3)
        except AttributeError as error:
            self.assertEqual(error.args[0], "The element does not exist")
        
    def test_to_list(self):
        root1 = node(1,1,node(0,0),node(2,2))
        self.assertEqual(to_list(root1), [[1, 1], [0, 0], [2, 2]])
        root2 = node('a',1,node('b',0),node('c',2))
        self.assertEqual(to_list(root2), [['a', 1], ['b', 0], ['c', 2]])

    
    def test_from_list(self):
        self.assertEqual(to_list(from_list([[1, 1], [0, 0], ['a', 2]])), [[1, 1], [0, 0], ['a', 2]])
            
    def test_conversion(self):
        root=from_list([[0,0],[2,2],['a',3]])
        self.assertEqual(to_list(root), [[0, 0], [2, 2], ['a', 3]])

    def test_find(self):
        self.assertEqual(find(node(1,1,node(0,1),node(2,2)),0), 1)
        self.assertEqual(find(node(1,1,node(0,1),node(2,2)),1), 1)
        self.assertEqual(find(node(1,1,node(0,1),node('a',2)),'a'), 2)

    def test_iterator(self) :
        root = node(1,2,node(0,1),node('a',3))
        list=to_list(root)
        itor=iterator(root)
        test=[]
        while itor.has_next():
            test.append(itor.__next__())
        self.assertEqual(test, list)

        self.assertRaises(StopIteration, lambda : itor.__next__())

    def test_filter(self):
        def func(k):
            if k%2==0:
                return True
            return False
        root = node(1,2,node(0,1),node('a',3))
        list=to_list(root)
        list2 = []
        for i in range(len(list)):
            if type(list[i][0]) is str :
                if func(ord(list[i][0])):
                    list2.append(list[i])
            else:
                if func(list[i][0]):
                    list2.append(list[i])

        itor=filter(root, func)
        test=[]
        while itor.has_next():
            test.append(itor.__next__())
        self.assertEqual(test, list2)

    def test_map(self):
        def func(k):
            k+1
        root = node(1,2,node(0,1),node('a',3))
        list=to_list(root)
        list2 = []
        for i in list:
            i[1] = func(i[1])
            list2.append(i)

        itor=map(root, func)
        test=[]
        while itor.has_next():
            test.append(itor.__next__())
        self.assertEqual(test, list2)

    def test_reduce(self):
        def func(k,j):
            return k+j
        root = node(1,2,node(0,1),node('a',3))
        sum=reduce(iterator(root), func)
        self.assertEqual(sum, 6)

    def test_dict(self):
        d=dict()
        d.setting(1,1)
        self.assertEqual(d.getting(1), 1)
        d.setting(0,0)
        self.assertEqual(d.getting(0), 0)
        d.setting('a', 5)
        self.assertEqual(d.getting('a'), 5)
        
    def test_mconcat(self):
        tree1=node(1,1,node(0,0),node(2,2))
        
        tree2 = node(-1,-1,node(4,1),node('a',2))

        forest=mconcat(tree1,tree2)
        self.assertEqual(to_list(forest), [[1, 1], [0, 0], [-1, -1], [2, 2], [4, 1], ['a', 2]])
    
    
    @given(st.lists(st.lists(st.integers(), min_size=2, max_size=2),max_size=1))
    def test_from_list_to_list_equality(self, test_List):
        self.assertEqual(to_list(from_list(test_List)), test_List)
    
    @given(st.lists(st.lists(st.integers(), min_size=2, max_size=2),max_size=1))
    def test_monoid_identity(self, test_List):
        self.assertEqual(to_list(mconcat(mempty(), from_list(test_List))), test_List)
        self.assertEqual(to_list(mconcat(from_list(test_List), mempty())), test_List)

if __name__ == '__main__':
    unittest.main()

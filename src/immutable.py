class node:

    def __init__(self,key,value,rightChild=None,leftChild=None):
        self.key=key
        self.value=value
        self.rightChild=rightChild
        self.leftChild=leftChild
        self.count=0



class treeIterator:

    def __init__(self,data):
        self.index=-1
        self.len=len(data)
        self.data=data
    def next(self):
        self.index+=1
        if self.len>self.index:
            return self.data[self.index]
        else:
            raise StopIteration
    def has_next(self):
        if self.len > self.index+1:
            return True
        else:
            return False

def add(tree,key,value):
    if tree.key == key:
        tree.value=value
        return True
    if tree.key > key:
        if tree.leftChild == None:
            tree.leftChild = node(key, value)
            return True
        else:
            return add(tree.leftChild,key,value)
    if tree.key < key:
        if tree.rightChild == None:
            tree.rightChild = node(key, value)
            return True
        else:
            return add(tree.rightChild,key, value)

def size(tree):
    if tree != None:
        tree.count=0
        tree.count+=1
        tree.count+=size(tree.rightChild)+size(tree.leftChild)
        return tree.count
    else:
        return 0

def from_list(list):
    if len(list)==0:
        return None
    temp = list.pop()
    root = node(temp[0], temp[1])
    while len(list)!=0:
        temp=list.pop()
        add(root,temp[0],temp[1])
    return root

def to_list(tree):
    list=[]
    def  func(node,list):
        if node!=None:
            func(node.leftChild,list)
            temp=[]
            temp.append(node.key)
            temp.append(node.value)
            list.append(temp)
            func(node.rightChild,list)
    func(tree,list)
    return list

def iterator(tree):
    list=to_list(tree)
    list2=[]
    for i in list:
        list2.append(i)
    return treeIterator(list2)

def find(tree,key):
    if tree.key==key:
        return tree.value
    if key < tree.key:
        if tree.leftChild == None:
            return None
        return find(tree.leftChild,key)
    if key > tree.key:
        if tree.leftChild == None:
            return None
        return find(tree.rightChild, key)

def filter(tree, func):
    list=to_list(tree)
    list2=[]
    for i in list:
        if func(i[0]):
             list2.append(i)
    return treeIterator(list2)

def map(tree, func):
    list=to_list(tree)
    list2=[]
    for i in list:
        i[1]=func(i[1])
        list2.append(i)
    return treeIterator(list2)

def reduce(treeitor,func):
    if treeitor.has_next():
        res=treeitor.next()[1]
    while treeitor.has_next():
        res=func(res,treeitor.next()[1])
    return res

def remove(tree, key):
    list=to_list(tree)
    for i in range(len(list)):
        if key==list[i][0]:
            list.pop(i)
            break
    return from_list(list)

def conact(t1,t2):
    l1=to_list(t1)
    l2=to_list(t2)
    l3=[]
    while (0<len(l1) and 0<len(l2)):
        if l1[0][0]<l2[0][0]:
            l3.append(l1.pop(0))
        elif l1[0][0]>l2[0][0]:
            l3.append(l2.pop(0))
        elif l1[0][0]==l2[0][0]:
            if l1[0][1]>l2[0][1]:
                l3.append(l2.pop(0))
                l1.pop(0)
            else:
                l3.append(l1.pop(0))
                l2.pop(0)
    while len(l1)>0:
        l3.append(l1.pop(0))
    while len(l2)>0:
        l3.append(l2.pop(0))
    return from_list(l3)

class dict():
    count=0
    root=None
    def getting(self,key):
        if self.count==0:
            return None
        else:
            return find(self.root,key)
    def setting(self,key,value):
        if self.count==0:
            self.root=node(key,value)
            self.count+=1
        else:
            add(self.root,key,value)



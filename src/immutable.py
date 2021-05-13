class node:

    def __init__(self, key, value, leftChild=None, rightChild=None):
        self.key = key
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.count = 0


class treeIterator:

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


def add(tree, key, value):
    if type(key) is str:
        key_int = ord(key)
        if tree.key == key_int:
            tree.value = value
            return True
        if tree.key > key_int:
            if tree.leftChild == None:
                tree.leftChild = node(key, value)
                return True
            else:
                return add(tree.leftChild, key, value)
        if tree.key < key_int:
            if tree.rightChild == None:
                tree.rightChild = node(key, value)
                return True
            else:
                return add(tree.rightChild, key, value)
    else:
        if tree.key == key:
            tree.value = value
            return True
        if tree.key > key:
            if tree.leftChild == None:
                tree.leftChild = node(key, value)
                return True
            else:
                return add(tree.leftChild, key, value)
        if tree.key < key:
            if tree.rightChild == None:
                tree.rightChild = node(key, value)
                return True
            else:
                return add(tree.rightChild, key, value)


def size(tree):
    if tree != None:
        tree.count = 1
        tree.count += size(tree.rightChild) + size(tree.leftChild)
        return tree.count
    else:
        return 0


def from_list(list):
    if len(list) == 0:
        return None
    if len(list) == 1:
        root = node(list[0][0], list[0][1])
    else:
        first = list[0]
        root = node(first[0], first[1])
        for i in list[1:]:
            add(root, i[0], i[1])
    return root


def to_list(tree):
    list = []

    def func(node, list):
        if node != None:
            temp_kv = []
            temp_kv.append(node.key)
            temp_kv.append(node.value)
            list.append(temp_kv)
            func(node.leftChild, list)
            func(node.rightChild, list)

    func(tree, list)
    return list


def iterator(tree):
    tree_list = to_list(tree)
    new_list = []
    for i in tree_list:
        new_list.append(i)
    return treeIterator(new_list)


def mempty():
    return None


def find(tree, key):
    if type(key) is str:
        key_int = ord(key)
        if type(tree.key) is str:
            if ord(tree.key) == key_int:
                return tree.value
            if key_int < ord(tree.key):
                if tree.leftChild == None:
                    return None
                return find(tree.leftChild, key)
            if key_int > ord(tree.key):
                if tree.leftChild == None:
                    return None
            return find(tree.rightChild, key)
        else:
            if tree.key == key_int:
                return tree.value
            if key_int < tree.key:
                if tree.leftChild == None:
                    return None
                return find(tree.leftChild, key)
            if key_int > tree.key:
                if tree.leftChild == None:
                    return None
            return find(tree.rightChild, key)
    else:
        if type(tree.key) is str:
            if ord(tree.key) == key:
                return tree.value
            if key < ord(tree.key):
                if tree.leftChild == None:
                    return None
                return find(tree.leftChild, key)
            if key > ord(tree.key):
                if tree.leftChild == None:
                    return None
            return find(tree.rightChild, key)
        else:
            if tree.key == key:
                return tree.value
            if key < tree.key:
                if tree.leftChild == None:
                    return None
                return find(tree.leftChild, key)
            if key > tree.key:
                if tree.leftChild == None:
                    return None
            return find(tree.rightChild, key)

    if tree.key == key:
        return tree.value
    if key < tree.key:
        if tree.leftChild == None:
            return None
        return find(tree.leftChild, key)
    if key > tree.key:
        if tree.leftChild == None:
            return None
        return find(tree.rightChild, key)


def filter(tree, func):
    tree_list = to_list(tree)
    new_list = []
    for i in tree_list:
        if type(i[0]) is str:
            if func(ord(i[0])):
                new_list.append(i)
        else:
            if func(i[0]):
                new_list.append(i)
    return treeIterator(new_list)


def map(tree, func):
    tree_list = to_list(tree)
    new_list = []
    for i in tree_list:
        i[1] = func(i[1])
        new_list.append(i)
    return treeIterator(new_list)


def reduce(treeitor, func):
    if treeitor.has_next():
        res = treeitor.__next__()[1]
    while treeitor.has_next():
        res = func(res, treeitor.__next__()[1])
    return res


def remove(tree, key):
    list = to_list(tree)
    count = 0
    for i in range(len(list)):
        if key == list[i][0]:
            count = 1
            list.pop(i)
            break
    if count == 0:
        raise AttributeError("The element does not exist")
    return from_list(list)


def mconcat(tree1, tree2):
    forest1 = to_list(tree1)
    forest2 = to_list(tree2)
    forest = []
    if forest1 == []:
        return from_list(forest2)
    if forest2 == []:
        return from_list(forest1)
    if forest1[0][0] > forest2[0][0]:
        forest = forest1 + forest2
    else:
        forest = forest2 + forest1
    return from_list(forest)


class dict():
    count = 0
    root = None

    def getting(self, key):
        if self.count == 0:
            return None
        else:
            return find(self.root, key)

    def setting(self, key, value):
        if self.count == 0:
            self.root = node(key, value)
            self.count += 1
        else:
            add(self.root, key, value)

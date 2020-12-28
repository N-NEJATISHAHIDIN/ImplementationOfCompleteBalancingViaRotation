import rootOfT
import numpy as np
from rootOfT import Node , treeQ

class CBT:
    def __init__(self, root):
        self.root = root

    def in_order(self, start, traversal):
        if start:
            traversal = self.in_order(start.left, traversal)
            traversal.append(start.data)
            traversal = self.in_order(start.right, traversal)
        return traversal


def arr_to_tree(arr, root, i, n):
    if i < n:
        temp = Node(arr[i])
        root = temp
        root.left = arr_to_tree(arr, root.left, 2*i+1, n)
        root.right = arr_to_tree(arr, root.left, 2*i+2, n)
    return root


def treeT():
    li = np.arange(1022)
    root = None
    root = arr_to_tree(li, root, 0, len(li))
    bst = CBT(root)
    arr = bst.in_order(root, [])
    return arr_to_tree(arr, None, 0, len(li))
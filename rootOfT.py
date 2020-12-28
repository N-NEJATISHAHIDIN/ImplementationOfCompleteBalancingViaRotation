#find root of T
import math
from random import randrange
from config import r_total

class Counter(object):
    counts = {}
    @staticmethod
    def count(func):
        def wrapped(*args,**kwargs):
            if func.__name__ in Counter.counts.keys():
                Counter.counts[func.__name__] += 1
            else:
                Counter.counts[func.__name__] = 0
            return func(*args,**kwargs)
        return wrapped

class Node:
    def  __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.sub = False
        self.rotate = False
        self.rotate_direction = 0
        # self.should_rotate_l = True
        # self.bf = 0

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)
        print("#################################################################")

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


def treeQ(node, node2):

    if (node2.data > node.data):
        if(node.right == None):
            node.right = node2
            node2.parent = node
        else :
            treeQ(node.right, node2)


    else:
        if(node.left == None):
            node.left = node2
            node2.parent = node
        else :
            treeQ(node.left, node2 )


def ifNodeExists(node, key):
    if (node.data == key):
        return node
    else:
        if(node.left!= None):
            result = ifNodeExists(node.left, key)
            if result!= None:
                return result
        if(node.right!= None):
            result1 = ifNodeExists(node.right, key)
            if result1!= None:
                return result1


def root_t(n):

    h = math.ceil(math.log(n+1, 2))
    # print(h)
    mar1 = 2**(h-1)
    mar2 = 2**(h-1) + 2**(h-2) - 2
    # print(mar1, mar2)


    if (n >= mar1 and n <= mar2) :
        return n - 2**(h-2) + 1

    mar3 = 2**(h-1) + 2**(h-2) -1
    mar4 = 2**h-1
    # print(mar3, mar4)

    if(n >= mar3 and n <= mar4):
        return 2**(h-1)

    return "Error: the hight does not match the number of nods."


class CBRTree:

    def __init__(self, root):
        self.root = root
        # rotate left at node x

    def insert(self, key):

        node =  Node(key)
        y = None
        x = self.root

        while x != None:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        # y is parent of x
        node.parent = y
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        # PART 2: re-balance the node if necessary
        self.__updateBalance(node)
@Counter.count
def leftRotate(x,root_tree):
    root = root_tree
    y = x.right
    x.right = y.left
    if y.left != None:
        y.left.parent = x

    y.parent = x.parent;
    if x.parent == None:
        root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left = x
    x.parent = y

    return root

@Counter.count
# rotate right at node x
def rightRotate(x,root_tree):
    root = root_tree
    y = x.left
    x.left = y.right;
    if y.right != None:
        y.right.parent = x
    
    y.parent = x.parent;
    if x.parent == None:
        root = y
    elif x == x.parent.right:
        x.parent.right = y
    else:
        x.parent.left = y
    
    y.right = x
    x.parent = y

    return root

def makePath_left(root,rootTree,f=0):
    print("root data",root.data,"   F",f)

    if(root.sub == 1):
        print("I should not be rotated")
    else:    
        if (f == 0 and root.left != None):
            while (root.left.left != None  and root.left.left.sub !=1 ):
                    rightRotate(root.left, rootTree)
            if(root.left != None):
                makePath_left(root.left,rootTree, 1)
        elif(f == 1 and root.right != None):
            while (root.right.left != None and root.right.left.sub !=1 and root.right.sub!=1):
                    rightRotate(root.right, rootTree)
            if(root.right != None):
                makePath_left(root.right,rootTree, 1)    

def makePath_right(root,rootTree,f=0):
    if(root.sub == 1):
        print("I should not be rotated")
    else:
        if (f == 0 and root.right != None):
            while (root.right.right != None and root.right.right.sub !=1 ):
                    leftRotate(root.right, rootTree)
            if(root.right != None):
                makePath_right(root.right,rootTree, 1)
        elif(f == 1 and root.left != None):
            while (root.left.right != None and root.left.right.sub !=1 and root.left.sub!=1):
                    leftRotate(root.left, rootTree)
            if(root.left != None):
                makePath_right(root.left,rootTree, 1)

def A_L(Q_root,rootTree, n):

    h = math.ceil(math.log(n+1, 2))
    s = h
    mar1 = 2**(h-1)
    mar2 = 2**(h-1) + 2**(h-2) - 2


    if (n >= mar1 and n <= mar2) :
        k = n - mar1 + 1
        temp = rootTree
        for i in range(k):
            if(i==0):
                leftRotate(temp.left,rootTree)
                temp = temp.left
            else:
                leftRotate(temp.right,rootTree)
                temp = temp.right
        s=h-1

    for j in range(s-2, 0, -1):
        k = 2**j-1
        temp = rootTree
        for i in range(k):
            if(i==0):
                leftRotate(temp.left,rootTree)
                temp = temp.left
            else:
                leftRotate(temp.right,rootTree)
                temp = temp.right

def A_R(Q_root,rootTree, n):

    h = math.ceil(math.log(n+1, 2))
    s = h
    mar1 = 2**(h-1) + 2**(h-2) 
    mar2 = 2**h-2

    
    if (n >= mar1 and n <= mar2) :
        temp = rootTree.right
        while(temp.left != None):
            temp = temp.left
        temp = temp.parent.parent
        k = n - mar1 
        p = n - 2**(h-1)
        for i in range(p-1,p-2*k-1,-2):
            rightRotate(temp,rootTree)
            temp = temp.parent.parent.parent


    if ( (math.log(n+1,2) - math.floor(math.log(n+1,2))) == 0):
        s = s-2
    else:
        s= s-3
    for j in range(s, 0, -1):
        k = 2**j-1
        temp = rootTree
        for i in range(k):
            if(i==0):
                rightRotate(temp.right,rootTree)
                temp = temp.right
            else:
                rightRotate(temp.left,rootTree)
                temp = temp.left


            
def PostorderTraversal(root):
    res = []
    if root:
        res = PostorderTraversal(root.left)
        res = res + PostorderTraversal(root.right)
        res.append(root.data)
    return res

def checkSubTree(root1, root2):
    if (PostorderTraversal(root1) == PostorderTraversal(root2)):
        if root1.left != None or root1.right != None :
            print("It is equal",root1.data)
            root1.sub = True
    else:
        if(root1.left != None and root2.left != None):
            checkSubTree(root1.left, root2.left)
        if(root1.right != None and root2.right != None):
            checkSubTree(root1.right, root2.right)

def checkSubTree(root1, root2):

    if(isSubtree(root2, root1)):
        print("It is equal",root1.data)
        root1.sub = 1
        # root1.sub = 2

    else:
        if(root1.left != None and (root1.left.right != None  or root1.left.right != None)):
            checkSubTree(root1.left, root2)
        if(root1.right != None and (root1.right.right != None  or root1.right.right != None)):
            checkSubTree(root1.right, root2)

# A function to do postorder tree traversal 
def rotatethem(root,rootTree): 
    if root: 
        rotatethem(root.left,rootTree) 
        rotatethem(root.right,rootTree) 
        if(root.rotate == True):
            if (root.rotate_direction == 0):
                rightRotate(root,rootTree)
            else:
                leftRotate(root,rootTree)


def generate_random_tree(tree):
    random_range = randrange(10)
    if(random_range != 1):
        random_range2 = randrange(2)
        if(random_range2 == 0):
            random_rotate = randrange(2)
            tree.rotate = True
            if(random_rotate == 0):
                tree.rotate_direction = 0
            else:
                tree.rotate_direction = 1

    if(tree.left != None and (tree.left.right != None  or tree.left.right != None)):
        generate_random_tree(tree.left)
    if(tree.right != None  and (tree.right.right != None  or tree.right.right != None)):
        generate_random_tree(tree.right)


def areIdentical(root1, root2): 
      
    # Base Case 
    if root1 is None and root2 is None: 
        return True
    if root1 is None or root2 is None: 
        return False
  
    # Check fi the data of both roots is same and data of 
    # left and right subtrees are also same 
    return (root1.data == root2.data and 
            areIdentical(root1.left , root2.left) and 
            areIdentical(root1.right, root2.right) 
            )  

def isSubtree(T, S): 
      
    # Base Case 
    if S is None: 
        return True
  
    if T is None: 
        return False
  
    # Check the tree with root as current node 
    if (areIdentical(T, S)): 
        return True
  
    # IF the tree with root as current node doesn't match 
    # then try left and right subtreee one by one 
    return isSubtree(T.left, S) or isSubtree(T.right, S) 





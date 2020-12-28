import random
import numpy as np
from rootOfT import Node , treeQ, ifNodeExists, root_t,rightRotate,leftRotate, makePath_left,makePath_right,A_L, A_R,PostorderTraversal,checkSubTree,generate_random_tree,rotatethem,isSubtree
from classCBT import treeT
from rootOfT import *
from random import randrange
from config import r_total
from rootOfT import Counter

def A1(n,tree_Q):
    #print tree
    tree_Q.display()
    #bild tree T

    #compute root of tree T
    root_T_data = root_t(n)-1
    print("root_T_data:",root_T_data)

    #find root of tree T in Q
    root_T_in_Q =ifNodeExists(tree_Q,root_T_data)

    #Move root T to the root of Q
    while(tree_Q != root_T_in_Q):
        if(root_T_in_Q.parent.right == root_T_in_Q ):
            tree_Q = leftRotate(root_T_in_Q.parent,tree_Q)
        else:
            tree_Q = rightRotate(root_T_in_Q.parent,tree_Q)

    #print tree
    tree_Q.display()

    #step 5
    makePath_left(tree_Q,tree_Q)
    makePath_right(tree_Q,tree_Q)

    #print tree
    tree_Q.display()

    #step 6
    A_L(tree_Q,tree_Q, n)
    A_R(tree_Q,tree_Q, n)

    #print tree
    tree_Q.display()
    return tree_Q
    

if __name__ == '__main__':

    # 1000,1100,1200
    n = 30

    #build tree Q
    l = list(range(n))
    random.shuffle(l)

    tree_1 = Node(l[0])
    for i in l[1:]:
        treeQ(tree_1, Node(i))

    tree_A1 = A1(n,tree_1)
    print(Counter.counts)
    l = list(range(n))
    random.shuffle(l)

    A2_tree_Q = Node(l[0])
    for i in l[1:]:
        treeQ(A2_tree_Q, Node(i))


    #build tree Q

    print("####################################")
    print("####################################")
    print("####################################")
    print("####################################")
    print("####################################")
    print("####################################")

    l = list(range(n))
    random.shuffle(l)

    tree_A2 = Node(l[0])
    for i in l[1:]:
        treeQ(tree_A2, Node(i))

    tree_A2 = A1(n,tree_A2)
    tree_A2.display()

    generate_random_tree(tree_A2)
    rotatethem(tree_A2,tree_A2)
    tree_A2.display()
    checkSubTree(tree_A2,tree_A1)
    makePath_left(tree_A2,tree_A2)
    makePath_right(tree_A2,tree_A2)
    tree_A2.display()






            
           



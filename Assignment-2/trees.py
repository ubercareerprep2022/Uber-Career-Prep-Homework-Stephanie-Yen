#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Created By  : Stephanie Yen
# Created Date: May 2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" TREES
    Functions that perform operations on tree data structures, and respective tests """  

### EXERCISE 1 ###

# Recursive definition of tree (provided)
class Tree:
    def __init__(self, root):
        self.root = root

    class TreeNode:
        def __init__(self, data, left, right):
            self.data = data
            self.left = left
            self.right = right

def printLevelOrder(root): 
    ''' Takes in the root of a tree and prints its level-order traversal. 
        Extra (not specified in assignment)                              '''
    if root is None: # sanity check
        return None

    q = [] # List implementation of queue, use to keep track of all nodes
    q.append(root)

    while q:
        levelSize = len(q)

        # print current level, go by node by node ...
        # 1) pop, 2) print, 3) enqueue children
        for i in range(levelSize): 
            # pop and print number associated with node
            currentNode = q.pop(0)
            print(currentNode.data, end=" ")

            # enqueue children 
            if currentNode.left:
                q.append(currentNode.left)
            if currentNode.right:
                q.append(currentNode.right)

def printInOrder(root):
    ''' Takes in the root of a tree and prints its in-order traversal. (LH -> root -> RH) '''
    if root is None: # base case
        return None
    
    printInOrder(root.left)
    print(root.data, end=" ")
    printInOrder(root.right)


def printPreOrder(root):
    ''' Takes in the root of a tree and prints its pre-order traversal. (root -> LH -> RH) '''
    if root is None: # base case
        return None
    
    print(root.data, end=" ")
    printPreOrder(root.left)
    printPreOrder(root.right)

def printPostOrder(root):
    ''' Takes in the root of a tree and prints its post-order traversal. (LH -> RH -> root) '''
    if root is None: # base case
        return None 
    
    printPostOrder(root.left)
    printPostOrder(root.right)
    print(root.data, end=" ")

### EXERCISE 2-3 ###

# Representing a hierarchical structure using a tree (provided)
class OrganizationStructure:
    def __init__(self, ceo):
        self.ceo = ceo # root

    class Employee: # node
        def __init__(self, name, title, directReports):
            self.name = name
            self.title = title
            self.directReports = directReports # List

def printLevelByLevel(org): 
    ''' 
    Takes in an organization structure and prints it level by level. 
    Each node is printed with the following format: 
        Name: A, Title: CEO
    Each level is separated by a newline.
    '''
    if org is None: # sanity check
        return None

    def printEmp(emp): 
        print("Name: {name}, Title: {title}".format(name = emp.name, title = emp.title))

    q = [] 
    q.append(org.ceo)

    while q: 
        levelSize = len(q) 

        for i in range(levelSize):
            currentEmp = q.pop(0)
            printEmp(currentEmp)

            if currentEmp.directReports:
                for report in currentEmp.directReports:
                    q.append(report)
            
        print("\n") # done with level
        
def printNumLevels(org):
    ''' 
    Takes in an organization structure and prints the number of levels in it.
    '''
    if org is None: # sanity check
        return None
    
    numLevels = 0
    q = []
    q.append(org.ceo) 

    while q:
        levelSize = len(q) 

        for i in range(levelSize):
            currentEmp = q.pop(0)

            if currentEmp.directReports:
                for report in currentEmp.directReports:
                    q.append(report) 
        
        numLevels += 1 # done with level

    print(numLevels)

# ----- TESTS -----

def main(): 
    leftChild = Tree.TreeNode(6, None, None)
    rightChild = Tree.TreeNode(3, None, None)
    left = Tree.TreeNode(7, None, None)
    right = Tree.TreeNode(17, leftChild, rightChild)
    root = Tree.TreeNode(1, left, right)
    tree = Tree(root)

    print("--- Testing traversal (print) methods ---")
    print("Level order")
    printLevelOrder(tree.root)  # 1 7 16 6 3
    print("\nIn-order")
    printInOrder(tree.root)     # 7 1 6 17 3
    print("\nPre-order")
    printPreOrder(tree.root)    # 1 7 17 6 3
    print("\nPost-order")
    printPostOrder(tree.root)   # 7 6 3 17 1

    print("\n")

    print("--- Testing organization structure methods ---")
    # Level 5
    empK = OrganizationStructure.Employee("K", "Sales Intern", None)
    # Level 4
    empJ = OrganizationStructure.Employee("J", "Sales Representative", [empK])
    empF = OrganizationStructure.Employee("F", "Engineer", None)
    empG = OrganizationStructure.Employee("G", "Engineer", None)
    empH = OrganizationStructure.Employee("H", "Engineer", None)
    # Level 3
    empI = OrganizationStructure.Employee("I", "Director", [empJ])
    empD = OrganizationStructure.Employee("D", "Manager", [empF, empG, empH])
    empE = OrganizationStructure.Employee("E", "Manager", None)
    # Level 2
    empB = OrganizationStructure.Employee("B", "CFO", [empI])
    empC = OrganizationStructure.Employee("C", "CTO", [empD, empE])
    # Level 1
    empA = OrganizationStructure.Employee("A", "CEO", [empB, empC])
    # organization
    org = OrganizationStructure(empA)
    print("Print level order")
    printLevelByLevel(org)
    print("Print number of levels")
    printNumLevels(org)


if __name__ == "__main__": 
    main()
#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Created By  : Stephanie Yen
# Created Date: April 2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" PART 4: LINKED LISTS 
    Data structure that supports common functionalities, and respective tests """  

# NOTE: Alternative implementation would use a 'dummy node' of which the next attribute is the 'head'
# NOTE: Can reduce shared logic via helper functions i.e., insert(), remove()

class Node: 
    def __init__(self, val, next=None): 
        self.val = val
        self.next = next
    
class LinkedList: 

    def __init__(self, head=None):
        self.head = head 
        self.tail = head # UPDATE
        self.numElements = 0
    
    def push(self, node):
        ''' Adds a node to the end of the list. '''
        if self.head is None: 
            self.head = self.tail = node
        else: 
            self.tail.next = node
            self.tail = self.tail.next
        
        self.numElements += 1 # increment size
    
    def pop(self): 
        ''' Removes and returns the value of the last node of the list. '''
        if self.head is None:
            return None

        currentNode = self.head
        while (currentNode.next.next is not None): # ALT: for i in range(self.numElements - 2)
            currentNode = currentNode.next 
        removedVal = currentNode.next.val # save the value of the last node
        currentNode.next = None # remove the last node
        self.numElements -= 1 # decrement size
        return removedVal

    def insert(self, index, node):
        ''' Adds a node at a specific index in the list, given that the index is less than or equal to the size of the list. 
            Assumes zero-indexing. '''
        if index < 0 or index > self.numElements: # check invalid indices
            return # assumption

        # special case: insert node at beginning of list
        if (index == 0):
            node.next = self.head
            self.head = node
            self.numElements += 1 # increment size

        # special case: insert node at end of text
        elif (index == self.numElements):
            self.push(node)
            
        else:
            counter = 1 # indicates index of the node that currentNode points to
            currentNode = self.head
            while (counter != index): # ALT: for i in range(index - 1)
                currentNode = currentNode.next 
                counter += 1
            # insert new node after currentNode
            node.next = currentNode.next
            currentNode.next = node

            self.numElements += 1 # increment size

    def remove(self, index):
        ''' Removes a node from a specific index in the list, if a node exists at that index. '''
        if index < 0 or index > self.numElements: # check invalid indices
            return # assumption

        # special case: remove node from beginning of list
        if (index == 0):
            self.head = self.head.next

        # special case: remove node from end of text
        elif (index == self.numElements):
            currentNode = self.head
            while (currentNode.next.next is not None):
                currentNode = currentNode.next 
            currentNode.next = None # remove the last node
            
        else:
            counter = 1 # indicates index of the node that currentNode points to
            currentNode = self.head
            while (counter != index): # ALT: for i in range(index - 1)
                currentNode = currentNode.next 
                counter += 1
            # remove the node after currentNode
            currentNode.next = currentNode.next.next
        
        self.numElements -= 1 # decrement size

    def elementAt(self, index):
        ''' Returns a pointer to the node at a specific index in the list, if a node exists at that index. 
            Assumes zero-indexing. '''
        if index < 0 or index >= self.numElements: # check invalid indices
            return # assumption

        # special case: element is at beginning of list
        if (index == 0):
            return self.head.val # assume we need the value
        
        else: 
            counter = 1 # indicates index of the node that currentNode points to
            currentNode = self.head
            while (counter != index):
                currentNode = currentNode.next 
                counter += 1
            # return the node after currentNode
            return currentNode.next.val # assume we need the value

    def size(self):
        ''' Returns the length of the list. '''
        return self.numElements

    def printList(self):
        ''' Returns a string representation of the linked list. '''
        if self.head is None: 
            return
        
        result = ""
        currentNode = self.head
        for i in range(self.numElements): 
            result += (str(currentNode.val) + ' -> ')
            currentNode = currentNode.next
        print(result)
        return result # assumption

    def hasCycle(self):  
        ''' Returns a boolean denoting whether a cycle exists in the list. '''
        if self.head is None: 
            return False # assumption
            
        nodes = set() # set of nodes in list (every node will be added)
        currentNode = self.head
        nodes.add(currentNode)

        while (currentNode.next is not None):
            currentNode = currentNode.next

            # we have found a cycle if the node is already in the set
            if currentNode in nodes:
                return True
            
            # add current node to set
            nodes.add(currentNode)
        
        # we have not found any repeated nodes
        return False


# ----- TESTS -----
# Tests for push, pop, insert, remove, elementAt
# These inherently test size and printList
# hasCycle is tested in main

def testPushBackAddsNode(list, node):
    ''' Tests whether a node can be pushed to the end of the list. '''
    list.push(node)
    list.printList()
    print("size: " + str(list.size()))

def testPopBackRemovesNode(list):
    ''' Tests whether a node can be popped from the end of the list. '''
    list.pop()
    list.printList()
    print("size: " + str(list.size()))

def testInsert(list, index, node):
    ''' Tests whether a node can be inserted at a valid index in the list. 
        (Does nothing if adding a node at an invalid index.) '''
    list.insert(index, node)
    list.printList()
    print("size: " + str(list.size()))

def testRemove(list, index):
    ''' Tests whether a node can be removed from a valid index in the list.
        (Does nothing if removing a node from an invalid index (no node).) '''
    list.remove(index) 
    list.printList()
    print("size: " + str(list.size()))

def testElementAt(list, index):
    ''' Tests whether a node can be returned when given its index. 
        (Returns nothing if given an invalid index (no node).) '''
    print(list.elementAt(index))

if __name__ == "__main__": 
    list = LinkedList()
    list.push(Node(1))
    list.push(Node(2))
    
    print("\ntest push and pop to/from back")
    testPushBackAddsNode(list, Node(3)) # 1 -> 2 -> 3 -> (size 3)
    testPopBackRemovesNode(list) # 1 -> 2 -> (size 2)

    print("\ntest insert and remove with valid indices")
    testInsert(list, 1, Node(4)) # 1 -> 4 -> 2 (size 3)
    testRemove(list, 1) # 1 -> 2 (size 2)

    print("\ntest insert and remove with invalid indices")
    # should do nothing and also return no errors
    testInsert(list, -1, Node(5))
    testInsert(list, 3, Node(5))
    testRemove(list, -1) 
    testRemove(list, 3) 

    print("\ntest element indexing")
    testElementAt(list, 0) # 1
    testElementAt(list, 1) # 2
    testElementAt(list, -1) # invalid index, returns None
    testElementAt(list, 2) # invalid index, returns None

    print("\ntest hasCycle")
    # no cycle (False)
    list.printList()
    print(list.hasCycle())

    # insert a cycle (True)
    list.head.next.next = list.head
    # list.printList()
    print(list.hasCycle())
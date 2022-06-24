#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Created By  : Stephanie Yen
# Created Date: May 2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" BINARY SEARCH TREES
    Functions that perform operations on tree data structures, and respective tests """  

### EXERCISE 4 ###

# Class definition of binary search tree
class BinarySearchTree:
    class Node: # when to nest?
        def __init__(self, key, left, right):
            self.key = key
            self.left = left
            self.right = right

    def __init__(self, root):
        self.root = root # Node
        
    def insert(self, key):
        ''' 
        Inserts a key into this binary search tree. 

        If there are n nodes in the tree, then the average runtime of 
        this method should be O(log(n)).

        @param (int) key The key to insert
        '''
        self.insertHelper(self.root, key)

    def insertHelper(self, root, key):
        # base case
        if root is None:
            return BinarySearchTree.Node(key)
        
        else: 
            if root.key == key: 
                return root 
            elif root.key < key: # need to insert to right
                root.right = self.insertHelper(root.right, key)
            else: # need to insert to left
                root.left = self.nsertHelper(root.left, key)
    
    def find(self, key):
        '''
        Checks whether or not a key exists in this binary search tree.

        If there are n nodes in the tree, then the average runtime of 
        this method should be O(log(n)).

        @param (int) key The key to check for
        @return (bool) True if the key is present in this tree, False otherwise
        '''
        self.findHelper(self.root, key)

    def findHelper(self, root, key):
        # base case
        if root is None:
            return False 
        
        else: 
            if root.key == key:
                return True 
            elif root.key < key: # need to search to the right
                self.findHelper(root.right, key) 
            else: # need to search to the left 
                self.findHelper(root.left, key)

        return False

### EXERCISE 5 ###

'''
 * Interface for a phone book.
 * Each entry in the phone book is made up of 2 components: a name (String) and a
 * phone number (long).
 * For the purposes of this exercise, you can assume that there are no duplicate names.
 *
 * For example, assume we have a phone book with the following data:
 *
 * {"name": "ABC", "phoneNumber": 1111111111}
 * {"name": "XYZ", "phoneNumber": 9999999999}
 * {"name": "DEF", "phoneNumber": 2222222222}
 *
 * then,
 * the size() method should return 3,
 * find("ABC") should return 1111111111,
 * find("XYZ") should return 9999999999,
 * find("PQR") should return -1.
 */
'''

# Implementation of the phone book interface using a List (ArrayList) data structure
class ListEntry:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

class ListPhoneBook:
    def __init__(self, size=0, phoneBook=[]): 
        self.size = size
        self.phoneBook = phoneBook # list of ListEntry objects

    def size(self): 
        '''
        @return (int) The number of entries in this phone book
        '''
        return self.size

    def insert(self, name, phoneNumber):
        '''
        Inserts an entry in this phone book.

        @param (String) name The name for the entry
        @param (long) phoneNumber The phone number for the entry
        '''
        self.phoneBook.append(ListEntry(name, phoneNumber))
        self.size += 1

    def find(self, name):
        '''
        * Returns the phone number associated with a name in the phone book.

        * @param (String) name The name to search for
        * @return (long) The phone number for the entry, or -1 if the name is not present in the phone book
        '''
        # iterate through all ListEntry objects in phonebook to find matching name
        for entry in self.phoneBook:
            if entry.name == name: 
                return entry.phoneNumber
        
        return -1

# Implementation of the phone book interface using a binary search tree data structure
class BSTEntry:
    def __init__(self, name, phoneNumber, left=None, right=None): 
        self.name = name
        self.phoneNumber = phoneNumber
        self.left = left 
        self.right = right

class BSTPhoneBook:
    def __init__(self, size=0, phoneBook=None):
        self.size = size
        self.phoneBook = phoneBook

    def size(self): 
        '''
        @return (int) The number of entries in this phone book
        '''
        return self.size

    def insert(self, name, phoneNumber):
        '''
        Inserts an entry in this phone book.

        @param (String) name The name for the entry
        @param (long) phoneNumber The phone number for the entry
        '''

    def find(self, name):
        '''
        * Returns the phone number associated with a name in the phone book.

        * @param (String) name The name to search for
        * @return (long) The phone number for the entry, or -1 if the name is not present in the phone book
        '''


# ----- TESTS -----

def main(): 
    return

if __name__ == "__main__": 
    main()
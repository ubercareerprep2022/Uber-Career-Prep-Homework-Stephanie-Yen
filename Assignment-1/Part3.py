#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Created By  : Stephanie Yen
# Created Date: March 2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" PART 3: STACKS & QUEUES
    Data structures that support common functionalities, and respective tests """  

class Node: 
    def __init__(self, val, next): 
        self.val = val
        self.next = next
class Stack: 

    def __init__(self, head=None, numElements=0, minElement=None):
        self.head = head # acts as top of stack
        self.numElements = numElements
        self.minElement = minElement
    
    def push(self, newVal):
        ''' Pushes an integer on top of the stack. '''
        # Add new node with new value to the beginning of the linked list
        newHead = Node(newVal, self.head)
        self.head = newHead

        # # Update minimum element if necesary
        # if self.numElements == 0: # stack is empty
        #     self.minElement = self.head
        # else: # stack is not empty
        #     if newVal < self.minElement.val: 
        #         self.minElement = self.head

        # Increment the size of the stack
        self.numElements += 1

    def pop(self):
        ''' Removes and returns the value of the top of the stack. '''
        # Return None if there is nothing in the stack
        if self.head is None: 
            return None

        # Remove the node at the beginning of the linked list
        oldHead = self.head
        self.head = oldHead.next # reset the head

        # Update minimum element if necessary
        # if oldHeadVal

        # Decrement the size of the stack
        self.numElements -= 1
        
        return oldHead.val
    
    def top(self): 
        ''' Returns the value of the top of the stack, without manipulating the stack. '''
        # Return None if there is nothing in the stack
        if self.head is None: 
            return None
        
        return self.head.val

    def isEmpty(self):
        ''' Returns True or False if the stack is empty or not empty, respectively. '''
        if (self.numElements == 0): return True
        else:                       return False

    def size(self):
        ''' Returns an integer value with the count of elements in the stack. '''
        return self.numElements
    
    # def min(): 
        ''' Returns the minimum element (node) of the stack in O(1) time. '''
        # return self.minElement

class Queue: 

    def __init__(self, head=None, tail=None, numElements=0):
        self.head = head # acts as front of queue
        self.tail = tail # acts as rear of queue
        self.numElements = numElements
        
    def enqueue(self, newVal):
        ''' Adds an item to the queue. '''
        # Add new node with new value to the end of the queue
        if self.isEmpty():
            self.head = Node(newVal, None)
            self.tail = Node(newVal, None)
        else: 
            newTail = Node(newVal, None)
            self.tail.next = newTail
            self.tail = newTail

        # Increment the size of the queue
        self.numElements += 1

    def dequeue(self):
        ''' Removes an item from the queue. '''
        # Return None if there is nothing in the queue
        if self.isEmpty(): 
            return None

        # Remove the node at the front of the queue
        oldHead = self.head
        self.head = oldHead.next # reset the head

        # Decrement the size of the stack
        self.numElements -= 1

        return oldHead.val
    
    def rear(self): 
        ''' Returns the item at the end of the queue. '''
        # Return None if there is nothing in the stack
        if self.isEmpty(): 
            return None
        
        return self.tail.val

    def front(self):
        ''' Returns the item at the front of the queue. '''
        if self.isEmpty(): 
            return None
        
        return self.head.val

    def size(self):
        ''' Returns an integer value with the count of elements in the queue. '''
        return self.numElements

    def isEmpty(self):
        ''' Returns whether or not the queue is empty. '''
        if (self.numElements == 0): return True
        else:                       return False


# ----- TESTS -----

if __name__ == "__main__": 
    print("--- TESTING STACK ---")
    myStack = Stack()
    myStack.push(42)
    print("Top of stack: " + str(myStack.top())) # 42
    print("Size of stack: " + str(myStack.size())) # 1
    print("Popped value: " + str(myStack.pop())) # 42
    print("Cannot pop if the stack is empty: " + str(myStack.pop())) # None
    print("Cannot peek if the stack is empty: " + str(myStack.top())) # None
    print("Size of stack: " + str(myStack.size())) # 0


    print("--- TESTING QUEUE ---")
    myQueue = Queue() 
    myQueue.enqueue(1)
    myQueue.enqueue(2)
    myQueue.enqueue(3)
    print("Size of queue: " + str(myQueue.size())) # 3
    print("Front of queue: " + str(myQueue.front())) # 1
    print("Rear of queue: " + str(myQueue.rear())) # 3
    print("Dequeue item: " + str(myQueue.dequeue())) # 1
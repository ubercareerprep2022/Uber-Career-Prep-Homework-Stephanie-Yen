#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Created By  : Stephanie Yen
# Created Date: April 2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" PART 5: REVERSE A LINKED LIST
    Three functions that reverse a linked list, and respective tests """  

from Part4 import Node, LinkedList

def reverseLinkedListIter(list):
    ''' Takes in a linked list and returns a new linked list with the same elements in reverse order. 
        Utilizes the iterative method. '''
    if list.head is None or list.head.next is None: # no need to reverse if 0 or 1 elements
        return
    
    prev = None 
    curr = list.head

    while curr != None:
        # before reversing the link, need to save the node after curr
        post = curr.next
        # reverse the link pointing out of curr
        curr.next = prev
        # move the node pointers
        prev = curr
        curr = post
    
    # return the newly reversed list
    list.head = prev # update the head pointer to the last node of og list
    return list

def reverseLinkedListStack(list):
    ''' Takes in a linked list and returns a new linked list with the same elements in reverse order. 
        Utilizes the stack method (with stacks implemented using Python lists). '''
    if list.head is None or list.head.next is None: # no need to reverse if 0 or 1 elements
        return
    
    # push all nodes (addresses of pointers) to a stack
    stack = []
    curr = list.head 

    while curr.next != None:
        stack.append(curr)
        curr = curr.next
    
    list.head = curr # update the head pointer to the last node of og list

    # pop elements from stack to create a reversed list
    while len(stack) != 0:
        curr.next = stack.pop()
        curr = curr.next
    
    curr.next = None # update the next pointer of the last node of reversed list 

    return list

def reverseLinkedListRecur(list):
    ''' Takes in a linked list and returns a new linked list with the same elements in reverse order. 
        Utilizes the recursive method. '''
    list.head = reverseHelper(list, list.head) # update the head pointer to the last node of og list
    return list

def reverseHelper(list, head):
    ''' Recursive helper function. '''
    # base case: 0 or 1 elements
    if head is None or head.next is None:
        return head 
    
    # reverse the rest of the list
    rest = reverseHelper(list, head.next)

    # update the head pointer to the last node of list
    head.next.next = head 
    head.next = None

    # return the new head pointer
    return rest

if __name__ == "__main__": 
    print("\nreversed list using iterative method")
    list1 = LinkedList()
    list1.push(Node(1))
    list1.push(Node(2))
    list1.push(Node(3))
    list1.printList()

    reverseList1 = reverseLinkedListIter(list1)
    reverseList1.printList()

    print("\nreversed list using stack method")
    list2 = LinkedList()
    list2.push(Node(4))
    list2.push(Node(5))
    list2.push(Node(6))
    list2.printList()

    reverseList2 = reverseLinkedListStack(list2)
    reverseList2.printList()

    print("\nreversed list using recursive method")
    list3 = LinkedList()
    list3.push(Node(7))
    list3.push(Node(8))
    list3.push(Node(9))
    list3.printList()

    reverseList3 = reverseLinkedListRecur(list3)
    reverseList3.printList()
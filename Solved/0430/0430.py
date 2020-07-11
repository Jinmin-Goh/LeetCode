# Problem No.: 430
# Solver:      Jinmin Goh
# Date:        20200712
# URL: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

import sys


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        pointer = head
        while True:            
            if pointer.child:
                temp = self.searchLast(pointer.child)                
                tempNext = pointer.next
                tempChild = pointer.child
                pointer.child = None
                pointer.next = tempChild
                if tempChild:
                    tempChild.prev = pointer
                temp.next = tempNext
                if tempNext:
                    tempNext.prev = temp
                pointer = temp
            if pointer.next:
                pointer = pointer.next
            else:
                break
        return head
    
    def searchLast(self, head: 'Node') -> 'Node':        
        pointer = head
        while True:            
            if pointer.child:
                temp = self.searchLast(pointer.child)                
                tempNext = pointer.next
                tempChild = pointer.child
                pointer.child = None
                pointer.next = tempChild
                if tempChild:
                    tempChild.prev = pointer
                temp.next = tempNext
                if tempNext:
                    tempNext.prev = temp
                pointer = temp
            if pointer.next:
                pointer = pointer.next
            else:
                break        
        return pointer
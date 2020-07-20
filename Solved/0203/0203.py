# Problem No.: 203
# Solver:      Jinmin Goh
# Date:        20200721
# URL: https://leetcode.com/problems/remove-linked-list-elements/

import sys

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            head = head.next
        if not head:
            return head
        
        pointer = head
        pointerNext = head.next
        
        if not pointerNext:
            if pointer.val == val:
                return None
            else:
                return head
        while pointer and pointerNext:
            while pointerNext and pointerNext.val == val:
                pointer.next = pointerNext.next
                pointerNext = pointer.next
            pointer = pointer.next
            if pointer:
                pointerNext = pointer.next
        return head
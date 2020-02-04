# Problem No.: 206
# Solver:      Jinmin Goh
# Date:        20200204
# URL: https://leetcode.com/problems/reverse-linked-list/

import sys

# iterative solution
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        ans = None
        walker = head
        walker2 = head.next
        while walker2:
            walker.next = ans
            ans = walker
            walker = walker2
            walker2 = walker2.next
        walker.next = ans
        ans = walker
            
        return ans
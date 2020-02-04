# Problem No.: 206
# Solver:      Jinmin Goh
# Date:        20200204
# URL: https://leetcode.com/problems/reverse-linked-list/

import sys

# recursive solution
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        self.ans = None
        self.walker = None
        self.recursive(head)
        return self.ans
    def recursive(self, head: ListNode) -> None:
        if not head:
            return
        self.recursive(head.next)
        if not self.ans:
            self.ans = head
            self.walker = self.ans
        else:
            head.next = None
            self.walker.next = head
            #print(self.ans, self.walker)
            self.walker = self.walker.next
            
# Problem No.: 142
# Solver:      Jinmin Goh
# Date:        20200126
# URL: https://leetcode.com/problems/linked-list-cycle-ii/

import sys

# No extra memory solution
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        walker = head
        while walker:
            if walker.val == None:
                return walker
            else:
                walker.val = None
            walker = walker.next
        return None
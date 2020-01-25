# Problem No.: 141
# Solver:      Jinmin Goh
# Date:        20200126
# URL: https://leetcode.com/problems/linked-list-cycle/

import sys

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        #print(id(head))
        #tempSet = set()
        walker = head
        while walker:
            if walker.val == None:
                return True
            else:
                walker.val = None
            walker = walker.next
        return False
# Problem No.: 141
# Solver:      Jinmin Goh
# Date:        20200126
# URL: https://leetcode.com/problems/linked-list-cycle/

import sys

# O(n) space solution
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        tempSet = set()
        walker = head
        while walker:
            if id(walker) in tempSet:
                return True
            else:
                tempSet.add(id(walker))
            walker = walker.next
        return False
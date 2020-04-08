# Problem No.: 876
# Solver:      Jinmin Goh
# Date:        20200408
# URL: https://leetcode.com/problems/middle-of-the-linked-list/

import sys

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        length = 0
        walker = head
        while walker:
            length += 1
            walker = walker.next
        length = length // 2
        walker = head
        for i in range(length):
            walker = walker.next
        return walker
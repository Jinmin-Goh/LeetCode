# Problem No.: 143
# Solver:      Jinmin Goh
# Date:        20200126
# URL: https://leetcode.com/problems/reorder-list/

import sys

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        walker = head
        nodeList = []
        while walker:
            nodeList.append(walker)
            walker = walker.next
            nodeList[-1].next = None
        walker = nodeList[0]
        while nodeList:
            if walker == head:
                nodeList.pop(0)
            else:
                walker.next = nodeList.pop(0)
                walker = walker.next
            if not walker or not nodeList:
                break
            walker.next = nodeList.pop()
            walker = walker.next
        
        """
        Do not return anything, modify head in-place instead.
        """
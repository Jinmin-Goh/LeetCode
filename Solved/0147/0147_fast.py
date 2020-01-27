# Problem No.: 147
# Solver:      Jinmin Goh
# Date:        20200127
# URL: https://leetcode.com/problems/insertion-sort-list/

import sys

# using python sort function
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        walker = head
        nodeList = []
        while walker:
            nodeList.append(walker.val)
            walker = walker.next
        nodeList.sort()
        i = 0
        walker = head
        while walker:
            walker.val = nodeList[i]
            walker = walker.next
            i += 1
        return head
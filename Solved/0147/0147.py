# Problem No.: 147
# Solver:      Jinmin Goh
# Date:        20200127
# URL: https://leetcode.com/problems/insertion-sort-list/

import sys

# insertion sort
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
            nodeList.append(walker)
            walker = walker.next
        for i in range(1, len(nodeList)):
            temp_i = i
            while temp_i > 0 and nodeList[temp_i].val < nodeList[temp_i - 1].val:
                nodeList[temp_i], nodeList[temp_i - 1] = nodeList[temp_i - 1], nodeList[temp_i]
                temp_i -= 1
        ans = nodeList[0]
        for i in range(len(nodeList) - 1):
            nodeList[i].next = nodeList[i + 1]
        nodeList[-1].next = None
        return ans
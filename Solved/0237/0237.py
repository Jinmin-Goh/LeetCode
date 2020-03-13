# Problem No.: 237
# Solver:      Jinmin Goh
# Date:        20200313
# URL: https://leetcode.com/problems/delete-node-in-a-linked-list/

import sys

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
        
            
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
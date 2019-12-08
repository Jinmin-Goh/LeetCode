# Problem No.: 19
# Solver:      Jinmin Goh
# Date:        20191209
# URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

import sys

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head.next == None:
            return None
        list_length = 0
        temp = head
        while temp:
            temp = temp.next
            list_length += 1
        target = list_length - n + 1
        temp = head
        # in case of head node
        if target == 1:
            head = head.next
        # in case of other node
        else:
            while target > 2:   # until before target node
                temp = temp.next
                target -= 1
            temp.next = temp.next.next
        return head
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
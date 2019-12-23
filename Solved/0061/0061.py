# Problem No.: 61
# Solver:      Jinmin Goh
# Date:        20191223
# URL: https://leetcode.com/problems/rotate-list/

import sys

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return head
        temp_p = head
        cnt = 1
        while temp_p.next:
            temp_p = temp_p.next
            cnt += 1
        k = k % cnt
        ans = head
        for i in range(cnt - k - 1):
            ans = ans.next
        temp_p.next = head
        temp = ans.next
        ans.next = None
        return temp
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
# Problem No.: 86
# Solver:      Jinmin Goh
# Date:        20200104
# URL: https://leetcode.com/problems/partition-list/

import sys

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        low = None
        high = None
        p_main_walk = head
        p_low_walk = None
        p_high_walk = None
        while p_main_walk:
            if p_main_walk.val < x:
                if not low:
                    low = p_main_walk
                    p_low_walk = low
                else:
                    p_low_walk.next = p_main_walk
                    p_low_walk = p_low_walk.next
            else:
                if not high:
                    high = p_main_walk
                    p_high_walk = high
                else:
                    p_high_walk.next = p_main_walk
                    p_high_walk = p_high_walk.next
            p_main_walk = p_main_walk.next
        if not low:
            return high
        if not high:
            return low
        p_low_walk.next = high
        p_high_walk.next = None
        return low
# Problem No.: 83
# Solver:      Jinmin Goh
# Date:        20200102
# URL: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

import sys

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        ans = None
        p_walk = head
        p_ans = None
        cur_val = None
        while p_walk:
            if not ans:
                ans = head
                p_ans = head
                cur_val = ans.val
                p_walk = p_walk.next
                continue
            if p_walk.val != cur_val:
                p_ans.next = p_walk
                p_ans = p_ans.next
                cur_val = p_walk.val
            p_walk = p_walk.next
        if p_ans.next:
            p_ans.next = None
        return ans
# Problem No.: 92
# Solver:      Jinmin Goh
# Date:        20200106
# URL: https://leetcode.com/problems/reverse-linked-list-ii/

import sys

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or not head.next or m == n:
            return head
        p_walk = head
        node_after_n = None
        node_before_m = None
        cnt = 1
        val_list = []
        while p_walk:
            if cnt == n + 1:
                node_after_n = p_walk
            if cnt == m - 1:
                node_before_m = p_walk
            if m <= cnt <= n:
                val_list.append(p_walk.val)
            p_walk = p_walk.next
            cnt += 1
        rev_head = None
        p_rev = None
        for i in reversed(range(len(val_list))):
            if not rev_head:
                rev_head = ListNode(val_list[i])
                p_rev = rev_head
            else:
                p_rev.next = ListNode(val_list[i])
                p_rev = p_rev.next
        if not node_before_m:
            p_rev.next = node_after_n
            return rev_head
        if not node_after_n:
            node_before_m.next = rev_head
            return head
        node_before_m.next = rev_head
        p_rev.next = node_after_n
        return head
# Problem No.: 160
# Solver:      Jinmin Goh
# Date:        20200201
# URL: https://leetcode.com/problems/intersection-of-two-linked-lists/

import sys

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        cnt1 = 0
        cnt2 = 0
        walker = headA
        while walker:
            cnt1 += 1
            walker = walker.next
        walker = headB
        while walker:
            cnt2 += 1
            walker = walker.next
        walker1 = headA
        walker2 = headB
        if cnt1 > cnt2:
            for i in range(cnt1 - cnt2):
                walker1 = walker1.next
        elif cnt1 < cnt2:
            for i in range(cnt2 - cnt1):
                walker2 = walker2.next
        while walker1 and walker2:
            if walker1 == walker2:
                return walker1
            walker1 = walker1.next
            walker2 = walker2.next
        return None
            
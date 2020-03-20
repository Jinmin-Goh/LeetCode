# Problem No.: 328
# Solver:      Jinmin Goh
# Date:        20200320
# URL: https://leetcode.com/problems/odd-even-linked-list/

import sys

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        oddHead = ListNode(head.val)
        evenHead = ListNode(head.next.val)
        oddFlag = True
        walker = head.next.next
        oddWalker = oddHead
        evenWalker = evenHead
        while walker:
            if oddFlag:
                oddWalker.next = ListNode(walker.val)
                oddWalker = oddWalker.next
            else:
                evenWalker.next = ListNode(walker.val)
                evenWalker = evenWalker.next
            walker = walker.next
            oddFlag = not oddFlag
        oddWalker.next = evenHead
        return oddHead
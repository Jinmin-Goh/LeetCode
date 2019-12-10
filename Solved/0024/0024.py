# Problem No.: 24
# Solver:      Jinmin Goh
# Date:        20191210
# URL: https://leetcode.com/problems/swap-nodes-in-pairs/submissions/

import sys

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        walker = head
        ans_head = None
        ans_walker = None
        temp = None
        # until list has least 2 nodes
        while walker and walker.next:
            if not ans_head:
                #print("before:",ans_head,ans_walker,head,walker)
                temp = ListNode(walker.next.val)
                ans_head = temp
                temp = ListNode(walker.val)
                ans_head.next = temp
                ans_walker = ans_head.next
                walker = walker.next.next
                #print("after:",ans_head,ans_walker,head,walker)
            else:
                temp = ListNode(walker.next.val)
                ans_walker.next = temp
                ans_walker = ans_walker.next
                temp = ListNode(walker.val)
                ans_walker.next = temp
                ans_walker = ans_walker.next
                walker = walker.next.next
        if walker:
            temp = ListNode(walker.val)
            ans_walker.next = temp
        return ans_head
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
# Problem No.: 23
# Solver:      Jinmin Goh
# Date:        20191210
# URL: https://leetcode.com/problems/merge-k-sorted-lists/submissions/

import sys

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        ans = None
        for i in lists:
            if ans == None:
                ans = i
            else:
                ans = self.mergeList(ans, i)
        return ans
                
    def mergeList(self, l1, l2):
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1
        walker = None
        head = None
        temp1 = l1
        temp2 = l2
        while temp1 and temp2:
            if head == None:
                #print("before:",temp1.val, temp2.val)
                if temp1.val < temp2.val:
                    head = temp1
                    walker = head
                    #walker.next = None
                    temp1 = temp1.next
                else:
                    head = temp2
                    walker = head
                    #walker.next = None
                    temp2 = temp2.next
                #print("after:",temp1.val, temp2.val)
            else:
                #print("before:",temp1.val, temp2.val)
                if temp1.val < temp2.val:
                    walker.next = temp1
                    walker = walker.next
                    temp1 = temp1.next
                else:
                    walker.next = temp2
                    walker = walker.next
                    temp2 = temp2.next
                #print("after:",temp1.val, temp2.val)
        if temp1:
            walker.next = temp1
        if temp2:
            walker.next = temp2
        return head
        
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
# Problem No.: 2
# Solver:      Jinmin Goh
# Date:        20191201
# URL: https://leetcode.com/problems/add-two-numbers/

import sys

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # make first number
        temp = l1
        num1 = 0
        cnt = 0
        while temp:
            num1 += temp.val * (10 ** cnt) 
            temp = temp.next
            cnt += 1
        
        # make second number
        temp = l2
        num2 = 0
        cnt = 0
        while temp:
            num2 += temp.val * (10 ** cnt) 
            temp = temp.next
            cnt += 1
        
        sumval = num1 + num2
        if sumval == 0:
            return ListNode(0)
        
        # making list nodes
        head = None
        current = None
        while sumval != 0:
            if not head:
                head = ListNode(sumval % 10)
                current = head
            else:
                current.next = ListNode(sumval % 10)
                current = current.next
            sumval = sumval // 10
            
        return head
        
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """     
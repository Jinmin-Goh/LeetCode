# Problem No.: 234
# Solver:      Jinmin Goh
# Date:        20200208
# URL: https://leetcode.com/problems/palindrome-linked-list/

import sys

# time: O(n) / space: O(1)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        if not head.next.next:
            if head.val == head.next.val:
                return True
            else:
                return False
        if not head.next.next.next:
            if head.val == head.next.next.val:
                return True
            else:
                return False
        # count total nodes
        walker = head
        length = 0
        while walker:
            length += 1
            walker = walker.next
        rightHalf = None
        walker = head
        # right half of listnode
        for i in range(length // 2):
            walker = walker.next
        rightHalf = walker
        if length % 2:
            rightHalf = rightHalf.next
        #print(rightHalf)
        # in case of odd nodes
        leftHalf = None
        walker1 = head
        walker2 = head.next
        temp = walker2.next
        walker1.next = None
        walker2.next = walker1
        for i in range(length // 2 - 2):
            walker1 = walker2
            walker2 = temp
            temp = temp.next
            walker2.next = walker1
        leftHalf = walker2
        #print(leftHalf, rightHalf)
        while leftHalf and rightHalf:
            if leftHalf.val != rightHalf.val:
                return False
            leftHalf = leftHalf.next
            rightHalf = rightHalf.next
        return True
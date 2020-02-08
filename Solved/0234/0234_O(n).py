# Problem No.: 234
# Solver:      Jinmin Goh
# Date:        20200208
# URL: https://leetcode.com/problems/palindrome-linked-list/

import sys

# time: O(n) / space: O(n)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        numList = []
        walker = head
        while walker:
            numList.append(walker.val)
            walker = walker.next
        for i in range(len(numList) // 2):
            if numList[i] != numList[-i - 1]:
                return False
        return True
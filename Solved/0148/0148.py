# Problem No.: 148
# Solver:      Jinmin Goh
# Date:        20200127
# URL: https://leetcode.com/problems/sort-list/

import sys

# mergesort, time O(n log n)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        walker = head
        valList = []
        while walker:
            valList.append(walker.val)
            walker = walker.next

        # mergesort can be changed into default sort function
        valList = self.mergeSort(valList)
        i = 0
        walker = head
        while walker:
            walker.val = valList[i]
            i += 1
            walker = walker.next
        return head
    
    def mergeSort(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        else:
            left = self.mergeSort(nums[:len(nums) // 2])
            right = self.mergeSort(nums[len(nums) // 2:])
            ans = []
            while left and right:
                if left[0] < right[0]:
                    ans.append(left.pop(0))
                else:
                    ans.append(right.pop(0))
            if left:
                ans += left
            else:
                ans += right
            return ans
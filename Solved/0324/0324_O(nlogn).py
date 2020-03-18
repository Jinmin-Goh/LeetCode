# Problem No.: 324
# Solver:      Jinmin Goh
# Date:        20200318
# URL: https://leetcode.com/problems/wiggle-sort-ii/

import sys

# time: O(n log n) / space: O(n)

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()
        temp = [None] * len(nums)
        cnt = 0
        for i in reversed(range((len(nums) - 1) // 2 + 1)):
            #print(temp, nums)
            temp[cnt] = nums[i]
            cnt += 2
        cnt = 1
        for i in reversed(range((len(nums) - 1) // 2 + 1, len(nums))):
            temp[cnt] = nums[i]
            cnt += 2
        for i in range(len(nums)):
            nums[i] = temp[i]
# Problem No.: 189
# Solver:      Jinmin Goh
# Date:        20200304
# URL: https://leetcode.com/problems/rotate-array/

import sys

# time: O(n) / space: O(n)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k == 0 or not nums:
            return
        k %= len(nums)
        temp = []
        for i in range(k):
            temp.append(nums[-k + i])
        for i in range(len(nums) - k):
            temp.append(nums[i])
        for i in range(len(temp)):
            nums[i] = temp[i]
        return
# Problem No.: 442
# Solver:      Jinmin Goh
# Date:        20200809
# URL: https://leetcode.com/problems/find-all-duplicates-in-an-array/

import sys

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        check = [0] * len(nums)
        for i in nums:
            check[i - 1] += 1
            
        ans = []
        for i in range(len(check)):
            if check[i] > 1:
                ans.append(i + 1)
        return ans
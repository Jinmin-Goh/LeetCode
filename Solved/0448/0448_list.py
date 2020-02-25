# Problem No.: 448
# Solver:      Jinmin Goh
# Date:        20200225
# URL: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

import sys

# time: O(n) / space: O(n)

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return 
        cnt = [False] * len(nums)
        for i in nums:
            cnt[i - 1] = True
        ans = []
        for i in range(len(cnt)):
            if not cnt[i]:
                ans.append(i + 1)
        return ans

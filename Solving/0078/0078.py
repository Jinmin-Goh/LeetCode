# Problem No.: 78
# Solver:      Jinmin Goh
# Date:        20191230
# URL: https://leetcode.com/problems/subsets/

import sys

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for i in nums:
            length = len(ans)
            for j in range(length):
                ans.append(ans[j][:] + [i])
        return ans
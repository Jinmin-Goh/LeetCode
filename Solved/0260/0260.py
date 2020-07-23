# Problem No.: 260
# Solver:      Jinmin Goh
# Date:        20200723
# URL: https://leetcode.com/problems/single-number-iii/

import sys

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = set()
        for i in nums:
            if i in ans:
                ans.remove(i)
            else:
                ans.add(i)
        return list(ans)
        
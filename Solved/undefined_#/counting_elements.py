# Problem No.: ???
# Solver:      Jinmin Goh
# Date:        20200407
# URL: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3289/

import sys

class Solution:
    def countElements(self, arr: List[int]) -> int:
        arrDict = {}
        for i in arr:
            if i not in arrDict:
                arrDict[i] = 1
            else:
                arrDict[i] += 1
        ans = 0
        for i in arrDict:
            if i in arrDict and i + 1 in arrDict:
                ans += arrDict[i]
        return ans
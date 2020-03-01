# Problem No.: 739
# Solver:      Jinmin Goh
# Date:        20200301
# URL: https://leetcode.com/problems/daily-temperatures/

import sys

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if len(T) == 1:
            return [0]
        ans = [0] * len(T)
        stack = []
        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i] :
                temp = stack.pop()
                ans[temp] = i - temp
            stack.append(i)
        return ans
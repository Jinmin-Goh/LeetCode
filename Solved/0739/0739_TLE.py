# Problem No.: 739
# Solver:      Jinmin Goh
# Date:        20200301
# URL: https://leetcode.com/problems/daily-temperatures/

import sys

# 27/37 passed and TLE

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0] * len(T)
        i = 0
        while i < len(T) - 1:
            if T[i] < T[i + 1]:
                ans[i] = 1
                i += 1
            else:
                temp = i
                cnt = 1
                while temp < len(T) - 1 and T[i] >= T[temp + 1]:
                    temp += 1
                    cnt += 1
                if temp == len(T) - 1:
                    i += 1
                # ascending exists
                else:
                    ans[i] = cnt
                    i += 1
        return ans
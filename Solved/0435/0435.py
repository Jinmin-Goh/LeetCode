# Problem No.: 435
# Solver:      Jinmin Goh
# Date:        20200816
# URL: https://leetcode.com/problems/non-overlapping-intervals/

import sys

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        n, cnt = len(intervals), 1
        if n == 0:
            return 0
        curr = intervals[0]
        
        for i in range(n):
            if curr[1] <= intervals[i][0]:
                curr = intervals[i]
                cnt += 1
                
        return n - cnt
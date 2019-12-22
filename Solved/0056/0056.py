# Problem No.: 56
# Solver:      Jinmin Goh
# Date:        20191221
# URL: https://leetcode.com/problems/merge-intervals/

import sys

class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        ans = []
        intervals.sort()
        for i in intervals:
            if not ans:
                ans.append(i)
            else:
                j = 0
                while j < len(ans):
                    if ans[j][1] >= i[0]:
                        if ans[j][1] < i[1]:
                            ans[j] = [ans[j][0],i[1]]
                        break
                    j += 1
                if j == len(ans):
                    ans.append(i)
        return ans
                        
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
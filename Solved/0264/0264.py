# Problem No.: 264
# Solver:      Jinmin Goh
# Date:        20200705
# URL: https://leetcode.com/problems/ugly-number-ii/

import sys

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = [1]
        p2 = 0
        p3 = 0
        p5 = 0
        
        while len(ans) < n:
            minVal = min(ans[p2] * 2, ans[p3] * 3, ans[p5] * 5)
            if minVal == ans[p2] * 2:
                p2 += 1
            if minVal == ans[p3] * 3:
                p3 += 1
            if minVal == ans[p5] * 5:
                p5 += 1
            ans.append(minVal)
            #print(p2, p3, p5, ans)
        return ans[-1]
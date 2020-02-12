# Problem No.: 279
# Solver:      Jinmin Goh
# Date:        20200212
# URL: https://leetcode.com/problems/perfect-squares/

import sys

# DP solution
# time: O(n^1.5), 6728 ms

class Solution:
    def numSquares(self, n: int) -> int:
        self.dpList = [None] * (n + 1)
        i = 1
        while i * i <= n:
            self.dpList[i * i] = 1
            i += 1
        return self.DP(n)
        
    def DP(self, n: int) -> int:
        #print(n, self.dpList)
        if not self.dpList[n]:
            cnt = 2 ** 31 - 1
            for i in reversed(range(1, int(n ** 0.5) + 1)):
                temp = 1 + self.DP(n - i * i)
                cnt = min(cnt, temp)
            self.dpList[n] = cnt
            
        return self.dpList[n]
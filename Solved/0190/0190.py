# Problem No.: 190
# Solver:      Jinmin Goh
# Date:        20200305
# URL: https://leetcode.com/problems/reverse-bits/

import sys

class Solution:
    def reverseBits(self, n: int) -> int:
        if n == 0:
            return 0
        ansStr = ""
        while n:
            ansStr += str(n % 2)
            n >>= 1
        while len(ansStr) < 32:
            ansStr += "0"
        #print(ansStr)
        ans = 0
        cnt = 1
        for i in reversed(range(32)):
            ans += int(ansStr[i]) * cnt
            cnt <<= 1
        return ans
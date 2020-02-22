# Problem No.: 338
# Solver:      Jinmin Goh
# Date:        20200222
# URL: https://leetcode.com/problems/counting-bits/

import sys

# time: O(n) / space: O(n)

class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        ans = [0]
        while len(ans) <= num + 1:
            temp = ans[:]
            for i in range(len(temp)):
                temp[i] += 1
            ans = ans + temp
        return ans[:num + 1]
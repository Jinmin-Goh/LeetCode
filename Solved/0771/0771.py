# Problem No.: 0771
# Solver:      Jinmin Goh
# Date:        20200502
# URL: https://leetcode.com/problems/jewels-and-stones/

import sys

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jSet = set()
        for i in J:
            jSet.add(i)
        ans = 0
        for i in S:
            if i in jSet:
                ans += 1
        return ans
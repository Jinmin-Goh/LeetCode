# Problem No.: 1046
# Solver:      Jinmin Goh
# Date:        20200412
# URL: https://leetcode.com/problems/last-stone-weight/

import sys

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            temp1 = stones.pop()
            temp2 = stones.pop()
            if temp1 > temp2:
                stones.append(temp1 - temp2)
            stones.sort()
        if stones:
            return stones[0]
        else:
            return 0
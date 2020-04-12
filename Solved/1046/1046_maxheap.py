# Problem No.: 1046
# Solver:      Jinmin Goh
# Date:        20200412
# URL: https://leetcode.com/problems/last-stone-weight/

import sys
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            temp1 = -heapq.heappop(stones)
            temp2 = -heapq.heappop(stones)
            if temp1 > temp2:
                heapq.heappush(stones, -(temp1 - temp2))
        if stones:
            return -stones[0]
        else:
            return 0
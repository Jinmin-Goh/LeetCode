# Problem No.: 275
# Solver:      Jinmin Goh
# Date:        20200618
# URL: https://leetcode.com/problems/h-index-ii/

import sys

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        n = len(citations)
        pFront = 0
        pRear = n - 1
        while pFront <= pRear:
            pMid = (pFront + pRear) // 2
            if n - pMid == citations[pMid]:
                return citations[pMid]
            if n - pMid < citations[pMid]:
                pRear = pMid - 1
            else:
                pFront = pMid + 1
        
        return n - pFront
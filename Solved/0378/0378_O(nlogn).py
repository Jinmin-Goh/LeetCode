# Problem No.: 378
# Solver:      Jinmin Goh
# Date:        20200328
# URL: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

import sys
import bisect

# binary search
# time: O(n log n) / space: O(1)

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pFront = matrix[0][0]
        pRear = matrix[-1][-1]
        while pFront < pRear:
            pMid = (pFront + pRear) // 2
            if sum(bisect.bisect_right(i, pMid) for i in matrix) < k:
                pFront = pMid + 1
            else:
                pRear = pMid
        return pFront
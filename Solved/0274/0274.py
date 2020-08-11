# Problem No.: 274
# Solver:      Jinmin Goh
# Date:        20200812
# URL: https://leetcode.com/problems/h-index/

import sys

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        cnt = 0
        for i in reversed(citations):
            if i > cnt:
                cnt += 1
        return cnt
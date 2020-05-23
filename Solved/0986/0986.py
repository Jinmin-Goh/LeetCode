# Problem No.: 986
# Solver:      Jinmin Goh
# Date:        20200524
# URL: https://leetcode.com/problems/interval-list-intersections/

import sys

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        aPos = 0
        bPos = 0
        ans = []
        while aPos < len(A) and bPos < len(B):
            if A[aPos][1] < B[bPos][0]:
                aPos += 1
            elif A[aPos][0] > B[bPos][1]:
                bPos += 1
            else:
                ans.append([max(A[aPos][0], B[bPos][0]), min(A[aPos][1], B[bPos][1])])
                if A[aPos][1] > B[bPos][1]:
                    bPos += 1
                else:
                    aPos += 1
        return ans
            
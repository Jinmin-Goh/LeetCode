# Problem No.: 973
# Solver:      Jinmin Goh
# Date:        20200531
# URL: https://leetcode.com/problems/k-closest-points-to-origin/

import sys

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distance = []
        for i in points:
            distance.append([i[0] ** 2 + i[1] ** 2, [i[0], i[1]]])
        distance.sort()
        ans = []
        for i in range(K):
            ans.append(distance[i][1])
        return ans
# Problem No.: 997
# Solver:      Jinmin Goh
# Date:        20200511
# URL: https://leetcode.com/problems/find-the-town-judge/

import sys

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trustedList = [[] for _ in range(N + 1)]
        trusterList = [[] for _ in range(N + 1)]
        for i in trust:
            trustedList[i[1]].append(i[0])
            trusterList[i[0]].append(i[1])
        for i in range(1, N + 1):
            if len(trustedList[i]) == N - 1 and not trusterList[i]:
                return i
        return -1
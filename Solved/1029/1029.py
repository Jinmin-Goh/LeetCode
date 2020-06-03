# Problem No.: 1029
# Solver:      Jinmin Goh
# Date:        20200603
# URL: https://leetcode.com/problems/two-city-scheduling/

import sys

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cnt = 0
        ans = 0
        AList = []
        BList = []
        for i in costs:
            ans += min(i)
            if i[0] > i[1]:
                AList.append(i[0] - i[1])
            else:
                BList.append(i[1] - i[0])
        if len(AList) == len(BList):
            return ans
        AList.sort()
        BList.sort()
        if len(AList) > len(BList):
            for i in range((len(AList) - len(BList)) // 2):
                ans += AList[i]
        else:
            for i in range((len(BList) - len(AList)) // 2):
                ans += BList[i]
        return ans
# Problem No.: 347
# Solver:      Jinmin Goh
# Date:        20200222
# URL: https://leetcode.com/problems/top-k-frequent-elements/

import sys

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = {}
        for i in nums:
            if i not in numDict:
                numDict[i] = (1, i)
            else:
                temp = numDict[i][0]
                numDict[i] = (temp + 1, i)
        cntList = list(numDict.values())
        cntList.sort()
        ans = []
        for i in range(k):
            ans.append(cntList[-i - 1][1])
        return ans
        
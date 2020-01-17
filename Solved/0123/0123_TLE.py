# Problem No.: 123
# Solver:      Jinmin Goh
# Date:        20200117
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

import sys


# 198/200 accepted and TLE solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minpos = 0
        minVal = prices[0]
        maxpos = 0
        maxVal = prices[0]
        minList = []
        maxList = []
        ans = 0
        for i in range(len(prices)):
            if prices[i] < maxVal:
                minList.append(prices[minpos])
                maxList.append(prices[maxpos])
                maxVal, minVal = prices[i], prices[i]
                maxpos, minpos = i, i
            else:
                maxVal = prices[i]
                maxpos = i
        if maxVal != minVal:
            minList.append(prices[minpos])
            maxList.append(prices[maxpos])
        if len(minList) == 0:
            return 0
        if len(minList) == 1:
            return maxList[0] - minList[0]
        if len(minList) == 2:
            return sum(maxList) - sum(minList)
        
        for i_front in range(len(minList) - 1):
            for i_rear in range(i_front, len(minList) - 1):
                for j_front in range(i_rear + 1, len(minList)):
                    for j_rear in range(j_front, len(minList)):
                        ans = max(ans, maxList[i_rear] - minList[i_front] + maxList[j_rear] - minList[j_front])
            
            
        return ans
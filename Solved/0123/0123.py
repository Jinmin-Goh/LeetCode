# Problem No.: 123
# Solver:      Jinmin Goh
# Date:        20200117
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        ascPos = None
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                ascPos = i
                break
        if ascPos == None:
            return 0
        prices = prices[i:]
        minpos = 0
        minVal = prices[0]
        maxpos = 0
        maxVal = prices[0]
        minmaxList = []
        ans = 0
        for i in range(len(prices)):
            if prices[i] < maxVal:
                minmaxList.append(prices[minpos])
                minmaxList.append(prices[maxpos])
                maxVal, minVal = prices[i], prices[i]
                maxpos, minpos = i, i
            else:
                maxVal = prices[i]
                maxpos = i
        if maxVal != minVal:
            minmaxList.append(prices[minpos])
            minmaxList.append(prices[maxpos])
        if len(minmaxList) == 0:
            return 0
        if len(minmaxList) == 2:
            return minmaxList[1] - minmaxList[0]
        if len(minmaxList) == 4:
            return minmaxList[3] + minmaxList[1] - minmaxList[2] - minmaxList[0]
        
        for i in range(2,len(minmaxList)):
            min1 = minmaxList[0]
            ans1 = 0
            min2 = minmaxList[i]
            ans2 = 0
            for j in range(i):
                min1 = min(min1, minmaxList[j])
                temp = minmaxList[j] - min1
                ans1 = max(ans1, temp)
            for j in range(i, len(minmaxList)):
                min2 = min(min2, minmaxList[j])
                temp = minmaxList[j] - min2
                ans2 = max(ans2, temp)
            ans = max(ans, ans1 + ans2)
        
        
        #for i_front in range(len(minList) - 1):
        #    for i_rear in range(i_front, len(minList) - 1):
        #        for j_front in range(i_rear + 1, len(minList)):
        #            for j_rear in range(j_front, len(minList)):
        #                ans = max(ans, maxList[i_rear] - minList[i_front] + maxList[j_rear] - minList[j_front])
            
            
        return ans
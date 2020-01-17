# Problem No.: 122
# Solver:      Jinmin Goh
# Date:        20200117
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minVal = prices[0]
        maxVal = prices[0]
        ans = 0
        tempAns = 0
        for i in prices:
            if i < maxVal:
                ans += maxVal - minVal
                maxVal, minVal = i, i
            else:
                maxVal = i
        if maxVal != minVal:
            ans += maxVal - minVal
        return ans
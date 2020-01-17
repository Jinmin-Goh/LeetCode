# Problem No.: 121
# Solver:      Jinmin Goh
# Date:        20200117
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minVal = prices[0]
        ans = 0
        
        for i in range(len(prices)):
            minVal = min(prices[i], minVal)
            temp = prices[i] - minVal
            if ans < temp:
                ans = temp
            
        return ans
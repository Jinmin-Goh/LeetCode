# Problem No.: 309
# Solver:      Jinmin Goh
# Date:        20200218
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

import sys

# good solution link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75930/Very-Easy-to-Understand-One-Pass-O(n)-Solution-with-No-Extra-Space
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        # initialize
        has1Stay = -prices[0]
        has1Sell = 0
        has0Stay = 0
        has0Buy = -prices[0]
        for i in range(1, len(prices)):
            tempHas1Stay = has1Stay
            tempHas1Sell = has1Sell
            tempHas0Stay = has0Stay
            tempHas0Buy = has0Buy
            has1Stay = max(tempHas1Stay, tempHas0Buy)
            has1Sell = prices[i] + max(tempHas1Stay, tempHas0Buy)
            has0Stay = max(tempHas0Stay, tempHas1Sell)
            has0Buy = -prices[i] + tempHas0Stay
            #print(has1Stay, has1Sell, has0Stay, has0Buy)
        return max(has1Sell, has0Stay)
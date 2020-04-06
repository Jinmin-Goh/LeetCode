# Problem No.: 188
# Solver:      Jinmin Goh
# Date:        20200407
# URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

import sys

# good solution link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/54113/A-Concise-DP-Solution-in-Java
# time: O(kn) / space: O(kn)

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        ans = 0
        
        # in case of maximum transactions can used
        if k >= len(prices) // 2:
            for i in range(1, len(prices)):
                if prices[i] > prices[i - 1]:
                    ans += prices[i] - prices[i - 1]
            return ans
        
        # in case of DP should used
        # dpTable[i][j] means maximum profit up to i transactions by time j
        # on time j, we can do nothing (dpTable[i][j] = dpTable[i][j - 1])
        # or, sell the stock. We must have bought it before.
        # in this case, t: 0 ~ j - 1 / max((prices[j] - prices[t]) + dpTable[i - 1][t - 1])
        # which is same to prices[j] + t:0~j-1 max(dpTable[i - 1][t - 1] + prices[t])
        dpTable = [[0] * len(prices) for _ in range(k + 1)]
        for i in range(1, k + 1):
            temp = -prices[0]
            for j in range(1, len(prices)):
                dpTable[i][j] = max(dpTable[i][j - 1], prices[j] + temp)
                temp = max(temp, dpTable[i - 1][j - 1] - prices[j])
        return dpTable[-1][-1]
        
# Problem No.: 518
# Solver:      Jinmin Goh
# Date:        20200607
# URL: https://leetcode.com/problems/coin-change-2/

import sys

# DP or unbounded knapsack problem
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        if not coins or amount < min(coins):
            return 0
        if amount == min(coins):
            return 1
        coins.sort()
        dpList = [0] * (amount + 1)
        dpList[0] = 1
        for i in coins:
            for j in range(1, amount + 1):
                if j >= i:
                    dpList[j] += dpList[j - i]
            #print(dpList)
        return dpList[-1]
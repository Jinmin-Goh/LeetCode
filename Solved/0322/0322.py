# Problem No.: 322
# Solver:      Jinmin Goh
# Date:        20200220
# URL: https://leetcode.com/problems/coin-change/

import sys

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        self.dpList = [None] * (amount + 1)
        coins.sort()
        return self.DP(coins, amount)
    
    def DP(self, coins: List[int], amount: int) -> int:
        if self.dpList[amount] == None:
            if amount < coins[0]:
                self.dpList[amount] = -1
            else:
                ans = 2 ** 31 - 1
                flag = False
                for i in reversed(coins):
                    if amount < i:
                        continue
                    elif amount == i:
                        return 1
                    temp = self.DP(coins, amount - i)
                    if temp == -1:
                        continue
                    ans = min(ans, temp + 1)
                    flag = True
                if flag:
                    self.dpList[amount] = ans
                else:
                    self.dpList[amount] = -1
        return self.dpList[amount]
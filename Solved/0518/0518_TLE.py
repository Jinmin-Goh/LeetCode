# Problem No.: 518
# Solver:      Jinmin Goh
# Date:        20200607
# URL: https://leetcode.com/problems/coin-change-2/

import sys

# naive TLE solution

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        if not coins or amount < min(coins):
            return 0
        if amount == min(coins):
            return 1
        coins.sort()
        dpList = [[] for _ in range(amount + 1)]
        #dpList[coins[0]] = 1
        for i in range(coins[0], amount + 1):
            for j in coins:
                if j > i:
                    break
                if j == i:
                    dpList[i].append([i])
                else:
                    for k in dpList[i - j]:
                        temp = k[:]
                        temp.append(j)
                        temp.sort()
                        if temp not in dpList[i]:
                            dpList[i].append(temp)
            #print(dpList)
        return len(dpList[-1])
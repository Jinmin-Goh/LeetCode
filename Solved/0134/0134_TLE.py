# Problem No.: 134
# Solver:      Jinmin Goh
# Date:        20200122
# URL: https://leetcode.com/problems/gas-station/

import sys

# 30/31 accepted TLE solution
# time: O(n^2)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        if not gas:
            return -1
        
        deltaList = []
        for i in range(len(gas)):
            deltaList.append(gas[i] - cost[i])
            
        for i in range(len(deltaList)):
            ansFlag = False
            if deltaList[i] >= 0:
                curGas = deltaList[i]
                temp = (i + 1) % len(deltaList)
                while curGas >= 0 and temp != i:
                    curGas += deltaList[temp]
                    temp = (temp + 1) % len(gas)
                if temp == i:
                    ansFlag = True
            if ansFlag:
                break
            
        if ansFlag:
            return i
        else:
            return -1
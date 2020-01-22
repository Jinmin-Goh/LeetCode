# Problem No.: 134
# Solver:      Jinmin Goh
# Date:        20200122
# URL: https://leetcode.com/problems/gas-station/

import sys

# time O(n) solution
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        if not gas:
            return -1
        
        deltaList = []
        for i in range(len(gas)):
            deltaList.append(gas[i] - cost[i])
        
        sumVal = 0
        minVal = 2 ** 31 - 1
        minIndex = None
        for i in range(len(deltaList)):
            sumVal += deltaList[i]
            if minVal > sumVal:
                minVal = sumVal
                minIndex = i
            
        return (minIndex + 1) % len(gas)

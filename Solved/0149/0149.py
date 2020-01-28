# Problem No.: 149
# Solver:      Jinmin Goh
# Date:        20200128
# URL: https://leetcode.com/problems/max-points-on-a-line/

import sys

import math
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        
        ans = 0
        for i in range(len(points) - 1):
            tempDict = {}
            tempMax = 0
            overlap = 0
            vertical = 0
            for j in range(i + 1, len(points)):
                # same point
                if (points[j][1] == points[i][1]) and (points[j][0] == points[i][0]):
                    overlap += 1
                    continue
                # vertical line
                elif points[j][0] == points[i][0]:
                    vertical += 1
                # normal line
                else:
                    xDel = (points[j][0] - points[i][0])
                    yDel = (points[j][1] - points[i][1])
                    slope = (xDel // self.gcd(xDel, yDel), yDel // self.gcd(xDel, yDel) )
                    if slope in tempDict:
                        tempDict[slope] += 1
                    else:
                        tempDict[slope] = 1
                    tempMax = max(tempMax, tempDict[slope])
                tempMax = max(tempMax, vertical)
            # tempMax represents maximum dots of i-th dot related line
            ans = max(ans, tempMax + overlap + 1)
        return ans
    
    def gcd(self, a: int, b: int) -> int:
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)
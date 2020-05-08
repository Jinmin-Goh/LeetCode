# Problem No.: 1232
# Solver:      Jinmin Goh
# Date:        20200508
# URL: https://leetcode.com/problems/check-if-it-is-a-straight-line/

import sys

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        point1 = coordinates[0]
        point2 = coordinates[1]
        if point2[0] == point1[0]:
            a = "inf"
            b = point1[0]
        else:
            a = (point2[1] - point1[1]) / (point2[0] - point1[0])
            b = point1[1] - a * point1[0]
        for i in range(1, len(coordinates)):
            if a == "inf":
                if coordinates[i][0] != point1[0]:
                    return False
            else:            
                if coordinates[i][0] == point1[0] or (coordinates[i][1] - point1[1]) / (coordinates[i][0] - point1[0]) != a:
                    return False
                if coordinates[i][1] - a * coordinates[i][0] != b:
                    return False
        return True
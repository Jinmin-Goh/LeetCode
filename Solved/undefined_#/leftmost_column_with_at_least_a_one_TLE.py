# Problem No.: ???
# Solver:      Jinmin Goh
# Date:        20200421
# URL: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3306/

import sys

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        temp = binaryMatrix.dimensions()
        nrow = temp[0]
        ncol = temp[1]
        
        if nrow * ncol <= 1000:
            for i in range(ncol):
                for j in range(nrow):
                    if binaryMatrix.get(j, i):
                        return i
            return -1
        for i in range(ncol):
            for j in range(nrow):
                if binaryMatrix.get(j, i):
                    return i
                
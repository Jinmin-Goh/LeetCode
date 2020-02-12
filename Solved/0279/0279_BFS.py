# Problem No.: 279
# Solver:      Jinmin Goh
# Date:        20200212
# URL: https://leetcode.com/problems/perfect-squares/

import sys

# BFS solution
# time: 1204 ms

class Solution:
    def numSquares(self, n: int) -> int:
        stack = [n]
        square = []
        i = 1
        while i * i <= n:
            square.append(i * i)
            i += 1
        cnt = 0
        while stack:
            temp = []
            cnt += 1
            for i in stack:
                for j in square:
                    if i - j == 0:
                        return cnt
                    elif i - j > 0:
                        temp.append(i - j)
                    else:
                        break
            stack = temp
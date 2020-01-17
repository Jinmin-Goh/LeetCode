# Problem No.: 120
# Solver:      Jinmin Goh
# Date:        20200117
# URL: https://leetcode.com/problems/triangle/

import sys


# O(n) time, O(n^2) space solution
# however, if we update dp table with temporary two lists, space will be O(n)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp_table = []
        for i in range(len(triangle)):
            dp_table.append([])
            for j in range(i + 1):
                if i == 0:
                    dp_table[-1].append(triangle[i][j])
                elif j == 0:
                    dp_table[-1].append(dp_table[i - 1][0] + triangle[i][0])
                elif j == i:
                    dp_table[-1].append(dp_table[i - 1][j - 1] + triangle[i][j])
                else:
                    dp_table[-1].append(triangle[i][j] + min(dp_table[i - 1][j - 1], dp_table[i - 1][j]))
        return min(dp_table[-1])
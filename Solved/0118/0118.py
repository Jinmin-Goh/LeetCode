# Problem No.: 118
# Solver:      Jinmin Goh
# Date:        20200115
# URL: https://leetcode.com/problems/pascals-triangle/

import sys

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        ans = [[1], [1,1]]
        for i in range(2, numRows + 1):
            print(ans, i)
            ans.append([1])
            for j in range(1, i - 1):
                ans[i].append(ans[i - 1][j - 1] + ans[i - 1][j])
            ans[i].append(1)
        ans.pop(1)
        return ans
            
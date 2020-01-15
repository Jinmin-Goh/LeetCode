# Problem No.: 119
# Solver:      Jinmin Goh
# Date:        20200115
# URL: https://leetcode.com/problems/pascals-triangle-ii/

import sys

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        ans = [1,1]
        while len(ans) < rowIndex + 1:
            temp = [1]
            for i in range(len(ans) - 1):
                temp.append(ans[i] + ans[i + 1])
            temp.append(1)
            ans = temp[:]
        return ans
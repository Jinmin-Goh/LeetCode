# Problem No.: 957
# Solver:      Jinmin Goh
# Date:        20200704
# URL: https://leetcode.com/problems/prison-cells-after-n-days/

import sys

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        if N == 0:
            return cells
        ansList = [cells[:]]
        ans = cells[:]
        cnt = 1
        while cnt <= N:
            temp = [0] * 8
            for j in range(1, 7):
                if ans[j - 1] == ans[j + 1]:
                    temp[j] = 1
            ans = temp[:]
            if temp in ansList:
                break
            else:
                ansList.append(temp)
            cnt += 1
        
        start = ansList.index(temp)
        length = cnt - start
            # maximum length of loop is 14, but why?
            # roughly 64(= 2 ** 8)
        N -= cnt
        N = N % length
        return ansList[start + N]
            
            
            
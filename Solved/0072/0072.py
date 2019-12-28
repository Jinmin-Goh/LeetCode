# Problem No.: 72
# Solver:      Jinmin Goh
# Date:        20191228
# URL: https://leetcode.com/problems/edit-distance/

import sys

# good solution link: https://leetcode.com/problems/edit-distance/discuss/159295/Python-solutions-and-intuition

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # top-down solution
        self.dp = {}
        ans = self.dpProcess(word1, word2, 0, 0)
        return ans
    
    def dpProcess(self, word1: str, word2: str, i: int, j: int):
        # if both string are empty
        if i == len(word1) and j == len(word2):
            return 0
        # if one string is empty
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i
        
        # memoization
        if (i,j) not in self.dp:
            temp = 0
            if word1[i] == word2[j]:
                temp = self.dpProcess(word1, word2, i + 1, j + 1)
            else:
                insert = 1 + self.dpProcess(word1, word2, i, j + 1)
                delete = 1 + self.dpProcess(word1, word2, i + 1, j)
                replace = 1 + self.dpProcess(word1, word2, i + 1, j + 1)
                temp = min(insert, delete, replace)
            self.dp[(i,j)] = temp
        return self.dp[(i,j)]
        
        # bottom-up solution
        """
    def minDistance(self, word1: str, word2: str) -> int:
        cnt_1 = len(word1)
        cnt_2 = len(word2)
        dp_table = [[0] * (cnt_2 + 1) for i in range(cnt_1 + 1)]
        
        for i in range(cnt_1 + 1):
            dp_table[i][0] = i
        for i in range(cnt_2 + 1):
            dp_table[0][i] = i
        
        for i in range(1, cnt_1 + 1):
            for j in range(1, cnt_2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp_table[i][j] = dp_table[i - 1][j - 1]
                else:
                    dp_table[i][j] = 1 + min(dp_table[i][j - 1], dp_table[i - 1][j], dp_table[i - 1][j - 1])
        return dp_table[cnt_1][cnt_2]
        """
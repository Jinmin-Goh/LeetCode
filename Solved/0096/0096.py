# Problem No.: 96
# Solver:      Jinmin Goh
# Date:        20200107
# URL: https://leetcode.com/problems/unique-binary-search-trees/

import sys

class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0:
            return 1
        self.dp_table = [None] * (n + 1)
        self.dp_table[0] = 1
        self.dp_table[1] = 1
        
        ans = self.makeFunc(1, n)
        return ans
    
    def makeFunc(self, start: int, end: int) -> int:
        if start > end:
            return 1
        if start == end:
            return 1
        if self.dp_table[end - start + 1]:
            return self.dp_table[end - start + 1]
        temp_ans = 0
        for i in range(start, end + 1):
            print(start, i, end)
            print(self.dp_table)
            if self.dp_table[i - start] == None:
                self.dp_table[i - start] = self.makeFunc(start, i - 1)
            if self.dp_table[end - i] == None:
                self.dp_table[end - i] = self.makeFunc(i + 1, end)
            temp_ans += self.makeFunc(start, i - 1) * self.makeFunc(i + 1, end)
        return temp_ans
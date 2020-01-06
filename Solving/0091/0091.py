# Problem No.: 91
# Solver:      Jinmin Goh
# Date:        20200106
# URL: https://leetcode.com/problems/decode-ways/

import sys

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        self.dp_table = [None] * len(s)
        self.haltFlag = False
        ans = self.dp(s)
        return ans
    
    def dp(self, s: str) -> int:
        if self.haltFlag:
            return 0
        if len(s) == 1:
            self.dp_table[0] = 1
            return 1
        elif len(s) == 2:
            # 30, 40, 50, ... case
            if 27 <= int(s[-2:]) and int(s[-2:]) % 10 == 0:
                self.haltFlag = True
                return 0
            # not 10, 20 and splitable case
            elif int(s) <= 26 and s[-1] != "0":
                self.dp_table[1] = 2
                return 2
            # single case
            else:
                self.dp_table[1] = 1
                return 1   
        else:
            # 00 or 30, 40, ... case
            if int(s[-2:]) == 0 or (27 <= int(s[-2:]) and int(s[-2:]) % 10 == 0):
                self.haltFlag = True
                return 0
            # ends with 26 < case
            if 27 <= int(s[-2:]) or s[-2] == "0":
                if not self.dp_table[len(s) - 1]:
                    self.dp_table[len(s) - 1] = self.dp(s[:-1])
                return self.dp_table[len(s) - 1]
            # 10, 20 case
            elif s[-1] == "0":
                if not self.dp_table[len(s) - 1]:
                    self.dp_table[len(s) - 1] = self.dp(s[:-2])
                return self.dp_table[len(s) - 1]
            # splitable case
            else:
                if not self.dp_table[len(s) - 1]:
                    self.dp_table[len(s) - 1] = self.dp(s[:-1]) + self.dp(s[:-2])
                return self.dp_table[len(s) - 1]
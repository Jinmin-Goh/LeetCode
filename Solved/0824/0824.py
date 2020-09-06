# Problem No.: 824
# Solver:      Jinmin Goh
# Date:        20200822
# URL: https://leetcode.com/problems/goat-latin/

import sys

class Solution:
    def toGoatLatin(self, S: str) -> str:
        SList = S.split()
        ans = ""
        cnt = 2
        for i in SList:
            if i[0] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
                temp = i
            else:
                temp = i[1:] + i[0]
            temp += "m" + "a" * cnt + " "
            ans += temp
            cnt += 1
        return ans[:-1]
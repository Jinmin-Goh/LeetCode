# Problem No.: 93
# Solver:      Jinmin Goh
# Date:        20200106
# URL: https://leetcode.com/problems/restore-ip-addresses/

import sys

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.ans = []
        self.searchFunc(s, 4, "")
        return self.ans
        
    def searchFunc(self, s: str, n: int, temp_ans: str) -> None:
        if n == 0 and len(s) == 0:
            self.ans.append(temp_ans)
            return
        elif n == 0 or len(s) < n or len(s) > 3 * n:
            return
        for i in range(min(3, len(s))):
            if int(s[:i + 1]) > 255 or (i > 0 and s[0] == "0"):
                continue
            if not temp_ans:
                temp = s[:i + 1]
            else:
                temp = temp_ans + "." + s[:i + 1]
            self.searchFunc(s[i + 1:], n - 1, temp)
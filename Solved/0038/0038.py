# Problem No.: 38
# Solver:      Jinmin Goh
# Date:        20191215
# URL: https://leetcode.com/problems/count-and-say/

import sys

class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return "1"
        else:
            temp = self.countAndSay(n - 1)
            i = 0
            temp_len = 0
            temp_char = None
            ans = ""
            while i < len(temp):
                if i == 0:
                    temp_len += 1
                    temp_char = temp[0]
                else:
                    if temp[i] == temp[i - 1]:
                        temp_len += 1
                    else:
                        ans += str(temp_len)
                        ans += temp_char
                        temp_len = 1
                        temp_char = temp[i]
                if i == len(temp) - 1:
                            ans += str(temp_len)
                            ans += temp_char
                i += 1
            return ans
        """
        :type n: int
        :rtype: str
        """
# Problem No.: 14
# Solver:      Jinmin Goh
# Date:        20191205
# URL: https://leetcode.com/problems/longest-common-prefix/

import sys

class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        minlen = (2 ** 31)-1
        ans = ""
        for i in range(len(strs)):
            if minlen > len(strs[i]):
                minlen = len(strs[i])
        for i in range(minlen):
            j = 0
            while j < len(strs) and strs[j][i] == strs[0][i]:
                j += 1
            if j == len(strs):
                ans += strs[0][i]
            else:
                break
        return ans
                
        """
        :type strs: List[str]
        :rtype: str
        """
        
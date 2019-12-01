# Problem No.: 3
# Solver:      Jinmin Goh
# Date:        20191201
# URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/

import sys

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # solve with sliding window algorithm
        p1 = 0
        p2 = 1
        maxlen = 0
        strlist = []
        i = 0
        if len(s) <= 1:
            return len(s)
        # convert string into list
        while not (i == len(s)):
            strlist.append(s[i])
            i += 1
        # adjust algorithm    
        while not(p1 == len(s)-1 and p2 == len(s)):
            # no repeating characters
            if len(strlist[p1:p2]) == len(set(strlist[p1:p2])):
                if p2 == len(s):
                    maxlen = max(maxlen, p2-p1)
                    break
                if maxlen < p2-p1:
                    maxlen = p2-p1
                p2 += 1
            else:
                p1 += 1
        return maxlen
                
        
        """
        :type s: str
        :rtype: int
        """
        
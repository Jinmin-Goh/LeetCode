# Problem No.: 438
# Solver:      Jinmin Goh
# Date:        20200225
# URL: https://leetcode.com/problems/find-all-anagrams-in-a-string/

import sys

# Sliding window algorithm
# time: O(n)

import copy
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        ans = []
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        pDict = {}
        sDict = {}
        for i in alphabet:
            pDict[i] = 0
            sDict[i] = 0
        for i in p:
            pDict[i] += 1
        for i in s[:len(p)]:
            sDict[i] += 1
        for i in range(len(s) - len(p)):
            if pDict == sDict:
                ans.append(i)
            sDict[s[i]] -= 1
            sDict[s[i + len(p)]] += 1
        if pDict == sDict:
            ans.append(i + 1)
        return ans
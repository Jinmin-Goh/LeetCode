# Problem No.: 1044
# Solver:      Jinmin Goh
# Date:        20200622
# URL: https://leetcode.com/problems/longest-duplicate-substring/

import sys
import collections

class Solution:
    def RabinKarp(self, S: str, pMid: int) -> bool:
        if pMid == 0:
            return (True, "")
        tempVal = 0
        for i in range(pMid):
            tempVal = (tempVal * self.powVal + ord(S[i])) % self.modVal
        
        mulVal = (1 << (8 * (pMid - 1))) % self.modVal
                    
        hashDict = collections.defaultdict(list)
        hashDict[tempVal].append(0)
        
        for i in range(1, len(S) - pMid + 1):
            tempVal = ((tempVal - ord(S[i - 1]) * mulVal) * self.powVal + ord(S[i + pMid - 1])) % self.modVal
            for j in hashDict[tempVal]:
                if S[i:i + pMid] == S[j:j + pMid]:
                    return (True, S[j:j + pMid])
            hashDict[tempVal].append(i)
        return (False, "")
    
    def longestDupSubstring(self, S: str) -> str:
        # appropriate prime
        self.modVal = 2147483647
        self.powVal = 256
        # binary search
        pFront = 0
        pRear = len(S)
        ans = ""
        while pFront + 1 < pRear:
            pMid = (pFront + pRear) // 2    
            flag = self.RabinKarp(S, pMid)
            if flag[0]:
                pFront = pMid
                ans = flag[1]
            else:
                pRear = pMid
        return ans
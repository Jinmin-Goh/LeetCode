# Problem No.: 278
# Solver:      Jinmin Goh
# Date:        20200501
# URL: https://leetcode.com/problems/first-bad-version/

import sys

# source code# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        # do binary search
        pFront = 1
        pRear = n
        while pFront < pRear:
            pMid = (pFront + pRear) // 2
            if isBadVersion(pMid):
                pRear = pMid
            else:
                pFront = pMid + 1
        return pFront
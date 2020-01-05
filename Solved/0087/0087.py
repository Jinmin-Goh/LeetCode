# Problem No.: 87
# Solver:      Jinmin Goh
# Date:        20200105
# URL: https://leetcode.com/problems/scramble-string/

import sys

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if sorted(s1) != sorted(s2):
            return False
        if s1 == s2:
            return True
        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[len(s2) - i:]) and self.isScramble(s1[i:], s2[:len(s2) - i]):
                return True
        return False
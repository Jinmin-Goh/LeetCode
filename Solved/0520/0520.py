# Problem No.: 520
# Solver:      Jinmin Goh
# Date:        20200801
# URL: https://leetcode.com/problems/detect-capital/

import sys

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        small = "abcdefghijklmnopqrstuvwxyz"
        if len(word) == 1:
            return True
        
        if word[0] in small:
            for i in word:
                if i in capital:
                    return False
            return True
        else:
            if word[1] in small:
                for i in word[1:]:
                    if i in capital:
                        return False
                return True
            else:
                for i in word[1:]:
                    if i not in capital:
                        return False
                return True
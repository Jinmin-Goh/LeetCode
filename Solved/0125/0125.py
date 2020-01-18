# Problem No.: 125
# Solver:      Jinmin Goh
# Date:        20200118
# URL: https://leetcode.com/problems/valid-palindrome/

import sys

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
        new_s = ""
        for i in s:
            if i in alphabet:
                new_s += i
        for i in range(len(new_s) // 2):
            if new_s[i] != new_s[-(1 + i)]:
                return False
        return True
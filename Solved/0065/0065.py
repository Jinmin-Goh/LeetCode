# Problem No.: 65
# Solver:      Jinmin Goh
# Date:        20191225
# URL: https://leetcode.com/problems/valid-number/

import sys

class Solution(object):
    def isNumber(self, s):
        if not s:
            return False
        s.strip()
        numFlag = False     # check number at front
        signFlag = False    # check sign at front 
        expFlag = False     # check e at middle
        expSignFlag = False # check sign behind e
        expNumFlag = False  # check number behind e
        floatFlag = False   # check decimal point at middle
        s = s.split()
        if len(s) != 1 :
            return False
        s = s[0]
        for i in range(len(s)):
            #print(s[i])
            # in case of sign
            if s[i] == "+" or s[i] == "-":
                if i != 0 and not expFlag:    # already number applied and before e sign
                    return False
                elif i == 0:
                    signFlag = True
                if s[i - 1] != "e" and expFlag:
                    return False
                else:
                    expSignFlag = True
            elif s[i] == "e":
                if not numFlag or expFlag:
                    return False
                else:
                    expFlag = True
            elif s[i] == ".":
                if floatFlag or expFlag:
                    return False
                else:
                    floatFlag = True
            else:
                try:
                    int(s[i])
                    if not expFlag or not numFlag:
                        numFlag = True
                    elif expFlag and not expNumFlag:
                        expNumFlag = True
                except ValueError:
                    return False
        # only e and nothing behind
        if expFlag and not expNumFlag:
            return False
        # no number
        if not numFlag:
            return False
        return True
        """
        :type s: str
        :rtype: bool
        """
        
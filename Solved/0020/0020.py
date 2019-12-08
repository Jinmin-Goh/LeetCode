# Problem No.: 20
# Solver:      Jinmin Goh
# Date:        20191209
# URL: https://leetcode.com/problems/valid-parentheses/

import sys

class Solution(object):
    def isValid(self, s):
        stack_list = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack_list.append(s[i])
            elif len(stack_list) == 0:
                return False
            elif s[i] == ')' and stack_list.pop() != '(':
                return False
            elif s[i] == '}' and stack_list.pop() != '{':
                return False
            elif s[i] == ']' and stack_list.pop() != '[':
                return False
        if len(stack_list):
            return False
        else:
            return True
        """
        :type s: str
        :rtype: bool
        """
        
# Problem No.: 32
# Solver:      Jinmin Goh
# Date:        20191213
# URL: https://leetcode.com/problems/longest-valid-parentheses/

import sys

class Solution(object):
    def longestValidParentheses(self, s):
        if not s:
            return 0
        s_list = []
        s_list_index = []
        s_list_binary = []
        left_cnt = 0
        right_cnt = 0
        for i in range(len(s)):
            s_list.append(s[i])
            s_list_index.append(i)
            s_list_binary.append(0)
            if s[i] == '(':
                left_cnt += 1
            else:
                right_cnt += 1
        while s_list and s_list[len(s_list)-1] == '(':
            s_list.pop()
            s_list_binary.pop()
            s_list_index.pop()
            left_cnt -= 1
        while s_list and s_list[0] == ')':
            s_list.pop(0)
            s_list_binary.pop()
            s_list_index.pop()
            right_cnt -= 1
        temp_p = 0
        if left_cnt > right_cnt and left_cnt * right_cnt > 0:
            while s_list[temp_p] == '(':
                temp_p += 1
            if temp_p > right_cnt:
                i = 0
                for i  in range(temp_p - right_cnt):
                    s_list.pop(0)
                    s_list_binary.pop()
                    s_list_index.pop()
        print(s_list, s_list_index, s_list_binary)
        
        self.findProcess(s_list, s_list_index, s_list_binary)
        
        ans = 0
        i = 0
        while i < len(s_list_binary):
            temp = 0
            while i < len(s_list_binary) and s_list_binary[i] == 1:
                temp += 1
                i += 1
            if ans < temp:
                ans = temp
            if temp == 0:
                i += 1
                
        return ans
    def findProcess(self, s_list, s_list_index, s_list_binary):
        if not s_list:
            return
        i = 0
        while i < len(s_list) - 1:
            if s_list[i] == '(' and s_list[i+1] == ')':
                s_list_binary[s_list_index[i]] = 1
                s_list_binary[s_list_index[i + 1]] = 1
                s_list.pop(i)
                s_list.pop(i)
                s_list_index.pop(i)
                s_list_index.pop(i)
                self.findProcess(s_list, s_list_index, s_list_binary)
                break
            else:
                i += 1
        """
        :type s: str
        :rtype: int
        """
        
# Problem No.: 76
# Solver:      Jinmin Goh
# Date:        20191230
# URL: https://leetcode.com/problems/minimum-window-substring/

import sys

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        for i in t:
            if i not in s:
                return ""
        t_list = [i for i in t]
        t_list = list(set(t_list))
        t_list.sort()
        pos_table = {}      # dictionary of how many alphabets are positioned
        cnt_table = {}      # count of t elements 
        for i in t_list:
            pos_table[i] = 0
            cnt_table[i] = 0
        for i in t:
            cnt_table[i] += 1
        
        p_front = 0
        p_rear = 0
        ans = ""
        cnt_element = 0     # count of satisfying unique alphabets in t
        while p_rear < len(s):
            temp_char = s[p_rear]
            if temp_char in pos_table:
                pos_table[temp_char] += 1
            if temp_char in cnt_table and cnt_table[temp_char] == pos_table[temp_char]:
                cnt_element += 1
            #print(pos_table, cnt_table, cnt_element)
            while p_front <= p_rear and cnt_element == len(cnt_table):
                temp_char = s[p_front]
                if not ans or len(ans) > p_rear - p_front + 1:
                    ans = s[p_front:p_rear + 1]
                if temp_char in pos_table:
                    pos_table[temp_char] -= 1
                if temp_char in cnt_table and cnt_table[temp_char] > pos_table[temp_char]:
                    cnt_element -= 1
                p_front += 1
            p_rear += 1
        return ans


"""
# right solution for 267/268 and TLE
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        for i in t:
            if i not in s:
                return ""
        t_list = [i for i in t]
        t_list = list(set(t_list))
        t_list.sort()
        pos_table = {}     # list dictionary of alphabet position
        cnt_table = {}
        for i in t_list
            pos_table[i] = []
            cnt_table[i] = 0
        for i in t:
            cnt_table[i] += 1
        #print(cnt_table)
        p_front = 0
        p_rear = 0
        initFlag = False
        temp_min = len(s)
        ans = ""
        for i in range(len(s)):
            if s[i] in t:
                # initializing position
                t_flag = True
                if cnt_table[s[i]] > len(pos_table[s[i]]):
                    pos_table[s[i]].append(i)
                # if update needed
                else:
                    pos_table[s[i]].pop(0)
                    pos_table[s[i]].append(i)
                if not initFlag:
                    for j in t_list:
                        if cnt_table[j] != len(pos_table[j]):
                            t_flag = False
                if t_flag:
                    initFlag = True
                #print(pos_table, cnt_table)
                # if all pos_table are filled
                if initFlag:
                    p_front = len(s)
                    p_rear = 0
                    for j in t_list:
                        p_front = min(min(pos_table[j]), p_front)
                        p_rear = max(max(pos_table[j]), p_rear)
                    if p_rear - p_front - 1 < temp_min:
                        ans = s[p_front:p_rear + 1]
                        temp_min = p_rear - p_front - 1
        return ans
           """         
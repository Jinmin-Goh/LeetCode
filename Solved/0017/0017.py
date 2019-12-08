# Problem No.: 17
# Solver:      Jinmin Goh
# Date:        20191208
# URL: https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/

import sys

class Solution(object):
    def letterCombinations(self, digits):
        if digits == "":
            return []
        ans = []
        num_dict = {'2':['a','b','c'],
                    '3':['d','e','f'],
                    '4':['g','h','i'],
                    '5':['j','k','l'],
                    '6':['m','n','o'],
                    '7':['p','q','r','s'],
                    '8':['t','u','v'],
                    '9':['w','x','y','z']}
        for i in range(len(digits)):
            if i == 0:
                ans += num_dict[digits[i]]
            else:
                temp_dict_list = num_dict[digits[i]]
                temp_ans_list = ans
                temp_new_ans_list = []
                for j in range(len(temp_dict_list)):
                    for k in range(len(temp_ans_list)):
                        temp_new_ans_list.append(temp_ans_list[k] + temp_dict_list[j])
                ans = temp_new_ans_list
        return ans
                
        """
        :type digits: str
        :rtype: List[str]
        """
        
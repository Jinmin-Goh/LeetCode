# Problem No.: 43
# Solver:      Jinmin Goh
# Date:        20191218
# URL: https://leetcode.com/problems/multiply-strings/

import sys

class Solution(object):
    def multiply(self, num1, num2):
        if num1 == '0' or num2 == '0':
            return '0'
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        ans = ""
        while p1 >= 0:
            p2 = len(num2) - 1
            temp_ans = ""
            while p2 >= 0:
                temp_p = len(num2) - p2 - 1
                temp_int = 0
                if not temp_ans:
                    temp_ans += str(int(num1[p1]) * int(num2[p2]))
                else:
                    temp_int = int(num1[p1]) * int(num2[p2])
                    if len(temp_ans) - temp_p == 1:
                        temp_ans = str(temp_int + int(temp_ans[0])) + temp_ans[1:]
                    else:
                        temp_ans = str(temp_int) + temp_ans
                p2 -= 1
            if ans == "":
                ans += temp_ans
            else:
                temp_ans += '0' * (len(num1) - p1 - 1)
                temp_sum = ""
                temp_p1 = len(ans) - 1
                temp_p2 = len(temp_ans) - 1
                over_10_flag = 0
                while temp_p1 >= 0 and temp_p2 >= 0:
                    temp_sum = str((int(ans[temp_p1]) + int(temp_ans[temp_p2]) + over_10_flag) % 10) + temp_sum
                    over_10_flag = (int(ans[temp_p1]) + int(temp_ans[temp_p2]) + over_10_flag) // 10
                    temp_p1 -= 1
                    temp_p2 -= 1
                if temp_p2 >= 0:
                    temp_sum = str(int(temp_ans[:temp_p2+1]) + over_10_flag) + temp_sum
                elif over_10_flag == 1:
                    temp_sum = "1" + temp_sum
                ans = temp_sum                
            p1 -= 1
        return ans
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
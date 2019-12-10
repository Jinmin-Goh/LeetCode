# Problem No.: 22
# Solver:      Jinmin Goh
# Date:        20191210
# URL: https://leetcode.com/problems/generate-parentheses/submissions/

import sys

class Solution(object):
    def generateParenthesis(self, n):
        left_cnt = n
        right_cnt = n
        ans = []
        self.DFS(left_cnt, right_cnt, ans, "")
        return ans

    def DFS(self, left_cnt, right_cnt, ans, string):
        if left_cnt > right_cnt:
            return
        if left_cnt == 0 and right_cnt == 0:
            ans.append(string)
            return
        if left_cnt:
            self.DFS(left_cnt - 1, right_cnt, ans, string + "(")
        if right_cnt:
            self.DFS(left_cnt, right_cnt - 1, ans, string + ")")
        """
        :type n: int
        :rtype: List[str]
        """
        
# Problem No.: 71
# Solver:      Jinmin Goh
# Date:        20191228
# URL: https://leetcode.com/problems/simplify-path/

import sys

class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return ""
        ans = "/"
        path_list = path.split("/")
        ans_list = []
        for i in path_list:
            if i == "" or i == ".":
                continue
            elif i == "..":
                try:
                    ans_list.pop()
                except IndexError:
                    continue
            else:
                ans_list.append(i)
        for i in ans_list:
            ans += i + "/"
        if ans == "/":
            return ans
        else:
            ans = ans[:len(ans) - 1]
                
        return ans
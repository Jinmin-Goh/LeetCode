# Problem No.: 89
# Solver:      Jinmin Goh
# Date:        20200105
# URL: https://leetcode.com/problems/gray-code/

import sys

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        self.ans = []
        self.searchFunc(n, [0], ["0" * n])
        return self.ans
    def searchFunc(self, n: int, ans: List[int], ans_binary: List[str]) -> None:
        if self.ans:
            return
        if len(ans) == 2 ** n:
            self.ans = ans[:]
            return
        for i in range(n):
            temp = ans[-1]
            temp_binary = ""
            if ans_binary[-1][i] == "0":
                temp += 2 ** (n - i - 1)
                temp_binary = ans_binary[-1][:i] + "1" + ans_binary[-1][i + 1:]
            else:
                temp -= 2 ** (n - i - 1)
                temp_binary = ans_binary[-1][:i] + "0" + ans_binary[-1][i + 1:]
            if temp in ans:
                continue
            else:
                temp_ans = ans[:]
                temp_ans.append(temp)
                temp_ans_binary = ans_binary[:]
                temp_ans_binary.append(temp_binary)
                self.searchFunc(n, temp_ans[:], temp_ans_binary[:])
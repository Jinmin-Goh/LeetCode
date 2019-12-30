# Problem No.: 77
# Solver:      Jinmin Goh
# Date:        20191230
# URL: https://leetcode.com/problems/combinations/

import sys

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return [[]]
        ans = []
        for i in range(k, n + 1) :
            for temp_ans in self.combine(i - 1, k - 1):
                ans.append(temp_ans + [i])
        return ans

"""
# correct for 26/27 and TLE
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k == 0:
            return [[]]
        if n < k:
            return []
        nList = [i + 1 for i in range(n)]
        if n == k:
            return [nList]
        if n == k:
            return [[i + 1] for i in range(n)]
        self.ans = []
        if n//2 > k:
            self.makeFunc(nList[:], k, [])
        else:
            self.delFunc(n-k, nList)
        return self.ans
    
    def makeFunc(self, nList: list, k: int, temp_ans: list) -> None:
        if k == 0:
            temp_ans.sort()
            if temp_ans not in self.ans:
                self.ans.append(temp_ans)
                return
            else:
                return
        else:
            for i in range(len(nList)):
                temp = nList[:]
                temp_temp_ans = temp_ans[:]
                temp_temp_ans.append(nList[i])
                temp.pop(i)
                self.makeFunc(temp[:], k-1, temp_temp_ans[:])
    def delFunc(self, k: int, temp_ans: list) -> None:
        if k == 0:
            temp_ans.sort()
            if temp_ans not in self.ans:
                self.ans.append(temp_ans)
                return
            else:
                return
        else:
            for i in range(len(temp_ans)):
                temp = temp_ans[:]
                temp.pop(i)
                self.delFunc(k-1, temp[:])
                """
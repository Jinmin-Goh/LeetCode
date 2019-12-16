# Problem No.: 40
# Solver:      Jinmin Goh
# Date:        20191216
# URL: https://leetcode.com/problems/combination-sum-ii/

import sys

class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        self.ans = []
        while candidates:
            self.solve(candidates, target, [])
            candidates.pop()
        return self.ans
    
    def solve(self, candidates, target, temp_ans):
        temp_cand = candidates[:]
        target -= temp_cand[len(temp_cand) - 1]
        if target >= 0:
            temp_ans.append(temp_cand[len(temp_cand) - 1])
        if target == 0:
            if temp_ans not in self.ans:
                self.ans.append(temp_ans)
            return
        if target < 0:
            return
        temp_cand.pop()
        while temp_cand:
            self.solve(temp_cand[:], target, temp_ans[:])
            temp_cand.pop()
    
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
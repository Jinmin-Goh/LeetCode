# Problem No.: 39
# Solver:      Jinmin Goh
# Date:        20191216
# URL: https://leetcode.com/problems/combination-sum/

import sys

class Solution(object):
    def combinationSum(self, candidates, target):
        if not candidates:
            return []
        self.ans = []
        candidates.sort()
        while candidates:
            self.search(candidates[:], target, [])
            candidates.pop()
        return self.ans
    
    def search(self, candidates, target, temp_ans):
        temp_cand = candidates[:]
        target -= temp_cand[len(temp_cand) - 1]
        if target == 0:
            temp_ans.append(temp_cand[len(temp_cand) - 1])
            self.ans.append(temp_ans)
            return
        if target > 0:
            temp_ans.append(temp_cand[len(temp_cand) - 1])
        if target < 0:
            return
        
        while temp_cand:
            self.search(temp_cand[:], target, temp_ans[:])
            temp_cand.pop()
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
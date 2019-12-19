# Problem No.: 47
# Solver:      Jinmin Goh
# Date:        20191219
# URL: https://leetcode.com/problems/permutations-ii/

import sys

class Solution(object):
    def permuteUnique(self, nums):
        if len(nums) < 2:
            return [nums]
        self.ans = []
        self.makeFunc(nums[:], [])
        return self.ans
        
        
    def makeFunc(self, nums, temp_ans):
        if not nums and temp_ans not in self.ans:
            self.ans.append(temp_ans)
            return
        for i in range(len(nums)):
            temp = nums[:]
            temp_temp_ans = temp_ans[:]
            temp_temp_ans += [nums[i]]
            temp.pop(i)
            #print(temp, temp_temp_ans)
            self.makeFunc(temp[:], temp_temp_ans[:])
        
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
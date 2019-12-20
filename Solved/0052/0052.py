# Problem No.: 52
# Solver:      Jinmin Goh
# Date:        20191220
# URL: https://leetcode.com/problems/n-queens-ii/

import sys

class Solution(object):
    def totalNQueens(self, n):
        ans = 0
        nums = [i for i in range(n)]
        candidate = self.permute(nums)
        for temp_cand in candidate:
            temp_1 = []
            temp_2 = []
            for i in range(len(temp_cand)):
                if (i + temp_cand[i]) not in temp_1:
                    temp_1.append(i + temp_cand[i])
                else:
                    break
                if (i - temp_cand[i]) not in temp_2:
                    temp_2.append(i - temp_cand[i])
                else:
                    break
            if len(temp_1) == n and len(temp_2) == n:
                ans += 1
        return ans
                
    
    def permute(self, nums):
        if len(nums) < 2:
            return [nums]
        self.ans = []
        self.makeFunc(nums[:], [])
        return self.ans
        
        
    def makeFunc(self, nums, temp_ans):
        if not nums:
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
        :type n: int
        :rtype: int
        """
        
# Problem No.: 90
# Solver:      Jinmin Goh
# Date:        20200105
# URL: https://leetcode.com/problems/subsets-ii/

import sys

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        nums.sort()
        for i in range(len(nums)):
            temp = []
            temp_ans = []
            for j in range(len(ans)):
                temp.append(ans[j][:])
            for j in range(len(temp)):
                if temp[j] + [nums[i]] not in temp or temp[j] + [nums[i]] not in ans:
                    temp_ans.append(temp[j] + [nums[i]])
            ans += temp_ans[:]
        return ans
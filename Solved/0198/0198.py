# Problem No.: 198
# Solver:      Jinmin Goh
# Date:        20200202
# URL: https://leetcode.com/problems/house-robber/

import sys

# dp solution
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        elif len(nums) == 3:
            return max(nums[1], nums[0] + nums[2])
        self.dp_list = [None] * len(nums)
        self.dp_list[0] = nums[0]
        self.dp_list[1] = max(nums[0], nums[1])
        self.dp_list[2] = max(nums[1], nums[0] + nums[2])
        return self.dp(nums)
        
    def dp(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return self.dp_list[len(nums) - 1]
        else:
            if self.dp_list[len(nums) - 4] == None:
                self.dp_list[len(nums) - 4] = self.dp(nums[:-3])            
            if self.dp_list[len(nums) - 3] == None:
                self.dp_list[len(nums) - 3] = self.dp(nums[:-2])
            self.dp_list[len(nums) - 1] = max((self.dp_list[len(nums) - 3] + nums[-1]), (self.dp_list[len(nums) - 3] + nums[-1]), (self.dp_list[len(nums) - 4] + nums[-2]))
            #print(nums, self.dp_list)
            return self.dp_list[len(nums) - 1]
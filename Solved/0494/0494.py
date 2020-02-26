# Problem No.: 494
# Solver:      Jinmin Goh
# Date:        20200226
# URL: https://leetcode.com/problems/target-sum/

import sys

# using memoization

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.dpDict = {}
        return self.DFS(nums, len(nums), 0, S)
        
    def DFS(self, nums: List[int], depth: int, curSum: int, S: int) -> int:
        if depth == 0:
            if curSum == S:
                return 1
            else:
                return 0
        else:
            if (depth, curSum) not in self.dpDict:
                pos = self.DFS(nums, depth - 1, curSum + nums[depth - 1], S)
                neg = self.DFS(nums, depth - 1, curSum - nums[depth - 1], S)
                self.dpDict[(depth, curSum)] = pos + neg
            return self.dpDict[(depth, curSum)]
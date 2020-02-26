# Problem No.: 494
# Solver:      Jinmin Goh
# Date:        20200226
# URL: https://leetcode.com/problems/target-sum/

import sys

# 61/139 passed and TLE
# time: O(2^n)

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.ans = 0
        self.DFS(nums, 1, 0, S)
        return self.ans
        
    def DFS(self, nums: List[int], depth: int, curSum: int, S: int) -> None:
        if depth == len(nums):
            if curSum + nums[depth - 1] == S:
                self.ans += 1
            if curSum - nums[depth - 1] == S:
                self.ans += 1
        else:
            self.DFS(nums, depth + 1, curSum + nums[depth - 1], S)
            self.DFS(nums, depth + 1, curSum - nums[depth - 1], S)
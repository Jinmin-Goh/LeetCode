# Problem No.: 384
# Solver:      Jinmin Goh
# Date:        20200330
# URL: https://leetcode.com/problems/shuffle-an-array/

import sys
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        randList = self.nums[:]
        random.shuffle(randList)
        return randList
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
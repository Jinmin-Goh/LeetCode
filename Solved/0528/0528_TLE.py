# Problem No.: 528
# Solver:      Jinmin Goh
# Date:        20200606
# URL: https://leetcode.com/problems/random-pick-with-weight/

import sys
import random

class Solution:
    def __init__(self, w: List[int]):
        self.nums = []
        for i in range(len(w)):
            self.nums += [i] * w[i]
        
    def pickIndex(self) -> int:
        return self.nums[random.randrange(len(self.nums))]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
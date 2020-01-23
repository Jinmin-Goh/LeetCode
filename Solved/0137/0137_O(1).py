# Problem No.: 137
# Solver:      Jinmin Goh
# Date:        20200123
# URL: https://leetcode.com/problems/single-number-ii/

import sys

# good solution: https://leetcode.com/problems/single-number-ii/discuss/43295/Detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers
# time: O(n) / space: O(1)
# we are excluding 3 times appeared and want to find only once appeared
# if number is appeared 3 times, we are excluding(make 0) with mask
# 3 -> 11(2)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x1 = 0
        x2 = 0
        mask = 0
        
        for i in nums:
            x2 ^= x1 & i
            x1 ^= i
            mask = ~(x1 & x2)
            x2 &= mask
            x1 &= mask
        return x1
# Problem No.: 136
# Solver:      Jinmin Goh
# Date:        20200123
# URL: https://leetcode.com/problems/single-number/

import sys

# 1) XOR is commutative, a ^ b = b ^ a. 
# 2) a number XOR by another number twice makes no change on original number, a ^ b ^ b = a
# so, only single element remains when we do all XOR for the lists

# using bit manipulation
# time: O(n) / space: O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans ^= i
        return ans
# Problem No.: 204
# Solver:      Jinmin Goh
# Date:        20200306
# URL: https://leetcode.com/problems/count-primes/

import sys

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        nums = [True] * (n)
        nums[0] = False
        nums[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if nums[i]:
                temp = i * 2
                while temp < n:
                    nums[temp] = False
                    temp += i
            #print(nums)
        return sum(nums)
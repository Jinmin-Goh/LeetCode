# Problem No.: 128
# Solver:      Jinmin Goh
# Date:        20200119
# URL: https://leetcode.com/problems/longest-consecutive-sequence/

import sys

# Time: O(n) solution
# if we use simple sort algorithm, time complexity is O(n log n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numSet = set(nums)
        ans = 1
        for i in nums:
            if i not in numSet:
                continue
            tempInt = i
            tempAns = 0
            while tempInt - 1 in numSet:
                tempInt -= 1
            while tempInt in numSet:
                numSet.remove(tempInt)
                tempInt += 1
                tempAns += 1
            ans = max(ans, tempAns)
        return ans
            
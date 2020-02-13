# Problem No.: 287
# Solver:      Jinmin Goh
# Date:        20200214
# URL: https://leetcode.com/problems/find-the-duplicate-number/

import sys

# Floyd's Tortoise and Hare Algorithm
#
# Proof:
#   start-----entry-------
#               |        |
#               --------meeting point
#   x: distance from start to entry
#   y: distance from entry to meeting point
#   c: cycle length
#
#   When tortoise and hare meets at meeting point,
#     tortoise traveled: x + y,
#     hare traveled: x + y + n*c (which is x + y + several loops inside the circle)
#
#   And hare is twice faster than tortoise, so
#     2(x + y) = x + y + n*c
#
#   Then we can get
#     x = n*c - y
#     x = (n-1)*c + (c-y)
#
#   Which means
#     traveling from start to entry (distance is x) and
#     traveling from meeting point to entry (c-y + several loops in circle)
#     will finally meet at entry

# time: O(n)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
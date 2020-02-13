# Problem No.: 287
# Solver:      Jinmin Goh
# Date:        20200213
# URL: https://leetcode.com/problems/find-the-duplicate-number/

import sys

# binary search solution
# time: O(n log n)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return 1
        front = 1
        mid = (len(nums) - 1) // 2
        back = len(nums) - 1
        while front <= mid <= back:
            if front == mid and mid == back:
                return mid
            cnt = 0
            for i in nums:
                if i <= mid:
                    cnt += 1
            if cnt > mid:
                back = mid
                mid = (front + back) // 2
            else:
                front = mid + 1
                mid = (front + back) // 2
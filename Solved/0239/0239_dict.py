# Problem No.: 239
# Solver:      Jinmin Goh
# Date:        20200210
# URL: https://leetcode.com/problems/sliding-window-maximum/

import sys

# time: O(n log k)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if k == 1:
            return nums
        if k == len(nums):
            return [max(nums)]
        maxVal = nums[0]
        queue = []
        ans = []
        queueDict = {}
        # initialize
        i = 0
        while i < k:
            queue.append(nums[i])
            if nums[i] not in queueDict:
                queueDict[nums[i]] = 1
            else:
                queueDict[nums[i]] += 1
            if maxVal < nums[i]:
                maxVal = nums[i]
            i += 1
        ans.append(maxVal)
        # move window
        while i < len(nums):
            temp = queue.pop(0)
            if queueDict[temp] == 1:
                del queueDict[temp]
            else:
                queueDict[temp] -= 1
            queue.append(nums[i])
            if nums[i] not in queueDict:
                queueDict[nums[i]] = 1
            else:
                queueDict[nums[i]] += 1
            maxVal = max(queueDict)
            ans.append(maxVal)
            i += 1
        return ans
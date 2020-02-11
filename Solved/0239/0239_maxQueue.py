# Problem No.: 239
# Solver:      Jinmin Goh
# Date:        20200211
# URL: https://leetcode.com/problems/sliding-window-maximum/

import sys

# time: O(n)
# implemented with maxQueue
class maxQueue:
    def __init__(self):
        self.maxDeque = []
        self.queue = []
        
    def push(self, x: int) -> None:
        while self.maxDeque and self.maxDeque[-1] < x:
            self.maxDeque.pop()
        self.maxDeque.append(x)
        self.queue.append(x)
    
    def pop(self) -> None:
        if self.maxDeque[0] == self.queue.pop(0):
            self.maxDeque.pop(0)
    
    def maxVal(self) -> int:
        return self.maxDeque[0]
    
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        window = maxQueue()
        ans = []
        i = 0
        while i < k:
            window.push(nums[i])
            i += 1
        ans.append(window.maxVal())
        while i < len(nums):
            window.pop()
            window.push(nums[i])
            ans.append(window.maxVal())
            i += 1
        
        return ans
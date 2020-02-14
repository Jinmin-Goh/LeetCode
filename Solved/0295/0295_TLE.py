# Problem No.: 295
# Solver:      Jinmin Goh
# Date:        20200214
# URL: https://leetcode.com/problems/find-median-from-data-stream/

import sys

# 17/18 passed and TLE
# O(n) for addNum

class MedianFinder:

    def __init__(self):
        self.nums = []
        self.midVal = 0

    def addNum(self, num: int) -> None:
        if not self.nums:
            self.nums.append(num)
            self.midVal = num
        elif len(self.nums) == 1:
            if self.nums[0] < num:
                self.nums.append(num)
            else:
                self.nums = [num] + self.nums
            self.midVal = (self.nums[0] + self.nums[1]) / 2
        else:
            flag = False
            for i in range(len(self.nums)):
                if self.nums[i] >= num:
                    flag = True
                    break
            if i == 0 and flag:
                self.nums = [num] + self.nums
            elif i == (len(self.nums) - 1) and not flag:
                self.nums.append(num)
            else:
                self.nums = self.nums[:i] + [num] + self.nums[i:]
            if len(self.nums) % 2:
                self.midVal = self.nums[len(self.nums) // 2]
            else:
                self.midVal = (self.nums[len(self.nums) // 2] + self.nums[len(self.nums) // 2 - 1]) / 2
        #print(self.nums, self.midVal)

    def findMedian(self) -> float:
        return self.midVal
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
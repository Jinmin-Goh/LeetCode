# Problem No.: ???
# Solver:      Jinmin Goh
# Date:        20200429
# URL: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3313/

import sys

class FirstUnique:
    def __init__(self, nums: List[int]):
        self.numDict = {}
        for i in nums:
            if i not in self.numDict:
                self.numDict[i] = 1
            else:
                self.numDict[i] += 1

    def showFirstUnique(self) -> int:
        for i in self.numDict:
            if self.numDict[i] == 1:
                return i
        return -1

    def add(self, value: int) -> None:
        if value not in self.numDict:
            self.numDict[value] = 1
        else:
            self.numDict[value] += 1

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
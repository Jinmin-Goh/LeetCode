# Problem No.: 155
# Solver:      Jinmin Goh
# Date:        20200129
# URL: https://leetcode.com/problems/min-stack/

import sys

# time: O(1)
class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = 2 ** 31 - 1
        
    def push(self, x: int) -> None:
        # if x is same or less than minVal, append second minVal first to record temporally and change minVal
        if x <= self.minVal:
            self.stack.append(self.minVal)
            self.minVal = x
        self.stack.append(x)
        
    def pop(self) -> None:
        if self.minVal == self.stack.pop():
            self.minVal = self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
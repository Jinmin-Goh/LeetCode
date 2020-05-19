# Problem No.: 901
# Solver:      Jinmin Goh
# Date:        20200520
# URL: https://leetcode.com/problems/online-stock-span/

import sys

class StockSpanner:
    def __init__(self):
        self.stack = []
        self.dpList = []

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append(price)
            self.dpList.append(1)
            return 1
        self.stack.append(price)
        if self.stack[-2] > price:
            self.dpList.append(1)
        else:
            self.dpList.append(self.dpList[-1] + 1)
        return self.dpList[-1]
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
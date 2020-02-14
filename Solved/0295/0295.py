# Problem No.: 295
# Solver:      Jinmin Goh
# Date:        20200214
# URL: https://leetcode.com/problems/find-median-from-data-stream/

import sys

# good solution: https://leetcode.com/problems/find-median-from-data-stream/discuss/74047/JavaPython-two-heap-solution-O(log-n)-add-O(1)-find
# using heapq, a minHeap library of Python
# O(log n) for addNum
from heapq import *

class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))
        #print(self.small, self.large)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2
        else:
            return self.large[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
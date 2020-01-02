# Problem No.: 84
# Solver:      Jinmin Goh
# Date:        20200102
# URL: https://leetcode.com/problems/largest-rectangle-in-histogram/

import sys

# simple, but slow solution. O(n^3)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        if len(heights) == 1:
            return heights[0]
        ans = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                ans = max(ans, (j - i + 1) * min(heights[i:j + 1]))
        return ans
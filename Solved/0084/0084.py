# Problem No.: 84
# Solver:      Jinmin Goh
# Date:        20200102
# URL: https://leetcode.com/problems/largest-rectangle-in-histogram/

import sys

# link: https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28917/AC-Python-clean-solution-using-stack-76ms
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # dummy height and stack value
        heights.append(0)
        stack = [-1]
        ans = 0
        # make ascending heights at the stack
        for i in range(len(heights)):
            print(ans, i, stack)
            # pop and caluculate area until heights[i] is max in stack
            while heights[i] < heights[stack[len(stack) - 1]]:
                h_val = heights[stack.pop()]
                w_val = i - stack[len(stack) - 1] - 1
                ans = max(ans, h_val * w_val)
            stack.append(i)
        return ans
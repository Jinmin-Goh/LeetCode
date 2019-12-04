# Problem No.: 11
# Solver:      Jinmin Goh
# Date:        20191204
# URL: https://leetcode.com/problems/container-with-most-water/submissions/

import sys

class Solution(object):
    def maxArea(self, height):
        p1 = 0
        p2 = len(height) - 1
        max_area = 0
        temp_area = 0
        temp_pointer = 0
        while p1 < p2:
            temp_pointer = 0
            temp_area = min(height[p1],height[p2]) * (p2 - p1)
            if temp_area > max_area:
                max_area = temp_area
            if height[p1] > height[p2]:
                temp_pointer = p2 - 1
                while height[p2] > height[temp_pointer] and p1 < p2:
                    temp_pointer -= 1
                p2 = temp_pointer
            else:
                temp_pointer = p1 + 1
                while height[p1] > height[temp_pointer] and p1 < p2:
                    temp_pointer += 1
                p1 = temp_pointer
        return max_area
        """
        :type height: List[int]
        :rtype: int
        """
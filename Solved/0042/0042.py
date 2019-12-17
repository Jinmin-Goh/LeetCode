# Problem No.: 42
# Solver:      Jinmin Goh
# Date:        20191217
# URL: https://leetcode.com/problems/trapping-rain-water/

import sys

class Solution(object):
    def trap(self, height):
        if len(height) < 3:
            return 0
        left_stack = []
        right_stack = []
        left_index_stack = []
        right_index_stack = []
        temp_max = 0
        # add max values from left
        i = 0
        while i < len(height):
            if height[i] >= temp_max:
                left_stack.append(height[i])
                left_index_stack.append(i)
                temp_max = height[i]
            i += 1
        temp_max = 0
        i = len(height) - 1
        # add max values from right
        while i >= 0:
            if height[i] >= temp_max:
                right_stack.append(height[i])
                right_index_stack.append(i)
                temp_max = height[i]
            if height[i] == left_stack[len(left_stack)-1]:
                break
            i -= 1
        print(left_stack, left_index_stack, right_stack, right_index_stack)
        # add water space from left
        ans = 0
        i = 0
        while i < len(left_stack) - 1:
            temp_i = left_index_stack[i] + 1
            temp_sum = 0
            while left_index_stack[i] < temp_i < left_index_stack[i + 1]:
                temp_sum += height[temp_i]
                temp_i += 1
            ans += (left_index_stack[i + 1] - left_index_stack[i] - 1) * left_stack[i] - temp_sum
            
            i += 1
        # add water space from left
        i = 0
        while i < len(right_stack) - 1:
            temp_i = right_index_stack[i] - 1
            temp_sum = 0
            while right_index_stack[i + 1] < temp_i < right_index_stack[i]:
                temp_sum += height[temp_i]
                temp_i -= 1
            ans += (right_index_stack[i] - right_index_stack[i + 1] - 1) * right_stack[i] - temp_sum
            
            i += 1    
            
        return ans
        """
        :type height: List[int]
        :rtype: int
        """
        
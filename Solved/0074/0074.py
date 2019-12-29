# Problem No.: 74
# Solver:      Jinmin Goh
# Date:        20191229
# URL: https://leetcode.com/problems/search-a-2d-matrix/

import sys

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        p_front = 0
        p_rear = len(matrix) - 1
        temp_ans = 0
        # find row first
        while matrix[p_front][0] < matrix[p_rear][0]:
            if matrix[(p_front + p_rear) // 2][0] == target:
                return True
            if p_rear - p_front == 1:
                if matrix[p_rear][0] <= target:
                    temp_ans = p_rear
                else:
                    temp_ans = p_front
                break
            elif matrix[(p_front + p_rear) // 2][0] > target:
                p_rear = (p_front + p_rear) // 2
            else:
                p_front = (p_front + p_rear) // 2
        # find target
        print(temp_ans)
        p_front = 0
        p_rear = len(matrix[0]) - 1
        while matrix[temp_ans][p_front] <= target <= matrix[temp_ans][p_rear]:
            if matrix[temp_ans][(p_front + p_rear) // 2] == target:
                return True
            elif matrix[temp_ans][(p_front + p_rear) // 2] > target:
                p_rear = (p_front + p_rear) // 2 - 1
            else:
                p_front = (p_front + p_rear) // 2 + 1
        return False                
        
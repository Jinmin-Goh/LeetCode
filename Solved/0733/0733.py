# Problem No.: 733
# Solver:      Jinmin Goh
# Date:        20200512
# URL: https://leetcode.com/problems/flood-fill/

import sys

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        original = image[sr][sc]
        stack = [(sr, sc)]
        while stack:
            temp = stack.pop()
            image[temp[0]][temp[1]] = newColor
            if temp[0] > 0 and image[temp[0] - 1][temp[1]] == original:
                stack.append((temp[0] - 1, temp[1]))
            if temp[0] < len(image) - 1 and image[temp[0] + 1][temp[1]] == original:
                stack.append((temp[0] + 1, temp[1]))
            if temp[1] > 0 and image[temp[0]][temp[1] - 1] == original:
                stack.append((temp[0], temp[1] - 1))
            if temp[1] < len(image[0]) - 1 and image[temp[0]][temp[1] + 1] == original:
                stack.append((temp[0], temp[1] + 1))
        return image
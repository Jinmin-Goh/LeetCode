# Problem No.: 437
# Solver:      Jinmin Goh
# Date:        20200224
# URL: https://leetcode.com/problems/path-sum-iii/

import sys

# 118/126 passed and TLE

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.ans = set()
        self.DFS(root, 0, "r", 0, sum)
        return len(self.ans)
        
    def DFS(self, root: TreeNode, curSum: int, path: str, depth: int, sum: int) -> None:
        if not root:
            return
        curSum += root.val
        path += str(depth)
        path += str(root.val)
        if path in self.ans:
            return
        if curSum == sum and path not in self.ans:
            self.ans.add(path)
        #print(self.ans, root.val, curSum, path)
        if root.left or root.right:
            if root.left:
                self.DFS(root.left, curSum, path + "L", depth + 1, sum)
                self.DFS(root.left, 0, "L", depth + 1, sum)
            if root.right:
                self.DFS(root.right, curSum, path + "R", depth + 1, sum)
                self.DFS(root.right, 0, "R", depth + 1, sum)
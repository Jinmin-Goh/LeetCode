# Problem No.: 543
# Solver:      Jinmin Goh
# Date:        20200412
# URL: https://leetcode.com/problems/diameter-of-binary-tree/

import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        if not root:
            return 0
        self.dfs(root)
        return self.ans
        
    def dfs(self, root: TreeNode) -> int:
        if not(root.left or root.right):
            return 0
        lVal = 0
        rVal = 0
        if root.left:
            lVal = self.dfs(root.left) + 1

        if root.right:
            rVal = self.dfs(root.right) + 1
        self.ans = max(self.ans, lVal + rVal)
        return max(rVal, lVal)
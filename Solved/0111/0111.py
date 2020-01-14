# Problem No.: 111
# Solver:      Jinmin Goh
# Date:        20200114
# URL: https://leetcode.com/problems/minimum-depth-of-binary-tree/

import sys

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.ans = None
        self.dfs(root, 1)
        return self.ans
        
    def dfs(self, root: TreeNode, level: int) -> None:
        if not root.left and not root.right:
            if not self.ans:
                self.ans = level
                return
            else:
                if self.ans > level:
                    self.ans = level
                return
        else:
            if self.ans and self.ans <= level:
                return
            else:
                if root.left:
                    self.dfs(root.left, level + 1)
                if root.right:
                    self.dfs(root.right, level + 1)
# Problem No.: 110
# Solver:      Jinmin Goh
# Date:        20200114
# URL: https://leetcode.com/problems/balanced-binary-tree/

import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.ans = True
        self.dfs(root)
        return self.ans
    
    def dfs(self, root: TreeNode) -> int:
        if not root or not self.ans:
            return 0
        lval = self.dfs(root.left)
        rval = self.dfs(root.right)
        if 1 < abs(lval - rval):
            self.ans = False
        return max(lval, rval) + 1
# Problem No.: 98
# Solver:      Jinmin Goh
# Date:        20200107
# URL: https://leetcode.com/problems/validate-binary-search-tree/

import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import math
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        self.flag = True
        self.dfs(root, -math.inf, math.inf)
        return self.flag
        
        
    def dfs(self, root: TreeNode, min_val: int, max_val: int) -> bool:
        if not self.flag:
            return
        if not root:
            return
        if root.left == None or min_val < root.left.val < root.val:
            self.dfs(root.left, min_val, root.val)
        else:
            self.flag = False
            return
        if root.right == None or max_val > root.right.val > root.val:
            self.dfs(root.right, root.val, max_val)
        else:
            self.flag = False
            return
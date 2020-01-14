# Problem No.: 112
# Solver:      Jinmin Goh
# Date:        20200114
# URL: https://leetcode.com/problems/path-sum/

import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        self.sum = sum
        return self.dfs(root, 0)
    
    def dfs(self, root: TreeNode, tempSum: int) -> bool:
        if not root.left and not root.right and tempSum + root.val == self.sum:
            return True
        elif not root.left and not root.right:
            return False
        else:
            tempLflag, tempRflag = False, False
            if root.left:
                tempLflag = self.dfs(root.left, tempSum + root.val)
            if root.right:
                tempRflag = self.dfs(root.right, tempSum + root.val)
            return tempLflag or tempRflag
# Problem No.: 337
# Solver:      Jinmin Goh
# Date:        20200221
# URL: https://leetcode.com/problems/house-robber-iii/

import sys

# 123/124 passed and TLE
# DFS solution, but no memoization

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        val = 0
        if root.right:
            val += self.rob(root.right.left) + self.rob(root.right.right)
        if root.left:
            val += self.rob(root.left.left) + self.rob(root.left.right)
        return max(val + root.val, self.rob(root.left) + self.rob(root.right))
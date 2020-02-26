# Problem No.: 543
# Solver:      Jinmin Goh
# Date:        20200226
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
        if not root or (not root.left and not root.right):
            return 0
        self.DFS(root)
        self.ans = 0
        self.DFS2(root)
        return self.ans
        
    def DFS(self, root: TreeNode) -> int:
        if not(root.left or root.right):
            return 0
        left = 0
        right = 0
        if root.left:
            left = self.DFS(root.left) + 1
        if root.right:
            right = self.DFS(root.right) + 1
        root.val = (left, right)
        return max(left, right)
    
    def DFS2(self, root: TreeNode) -> None:
        if not(root.left or root.right):
            return
        self.ans = max(self.ans, root.val[0] + root.val[1])
        if root.left:
            self.DFS2(root.left)
        if root.right:
            self.DFS2(root.right)
        
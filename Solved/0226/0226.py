# Problem No.: 226
# Solver:      Jinmin Goh
# Date:        20200207
# URL: https://leetcode.com/problems/invert-binary-tree/

import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        self.DFS(root)
        return root
    
    def DFS(self, root: TreeNode) -> None:
        if not root.right and not root.left:
            return
        else:
            root.left, root.right = root.right, root.left
            if root.left:
                self.DFS(root.left)
            if root.right:
                self.DFS(root.right)
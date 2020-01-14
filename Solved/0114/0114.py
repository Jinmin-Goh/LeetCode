# Problem No.: 114
# Solver:      Jinmin Goh
# Date:        20200114
# URL: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return root
        self.list = []
        self.inorder(root)
        temp = root
        root.left = None
        for i in range(1,len(self.list)):
            temp.right = TreeNode(self.list[i])
            temp = temp.right
        
    def inorder(self, root: TreeNode) -> None:
        if not root:
            return
        self.list.append(root.val)
        if root.left:
            self.inorder(root.left)
        if root.right:
            self.inorder(root.right)
        """
        Do not return anything, modify root in-place instead.
        """
        
# Problem No.: 94
# Solver:      Jinmin Goh
# Date:        20200106
# URL: https://leetcode.com/problems/binary-tree-inorder-traversal/

import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.ans = []
        self.searchFunc(root)
        return self.ans
    
    def searchFunc(self, root: TreeNode) -> None:
        if root.left:
            self.searchFunc(root.left)
        self.ans.append(root.val)
        if root.right:
            self.searchFunc(root.right)
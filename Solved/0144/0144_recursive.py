# Problem No.: 144
# Solver:      Jinmin Goh
# Date:        20200126
# URL: https://leetcode.com/problems/binary-tree-preorder-traversal/

import sys

# recursive preorder traversal solution
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.find(root, [])
        
    def find(self, root: TreeNode, tempAns: List[int]) -> List[int]:
        if not root:
            return tempAns
        tempAns.append(root.val)
        if root.left:
            tempAns = self.find(root.left, tempAns)
        if root.right:
            tempAns = self.find(root.right, tempAns)
        return tempAns
        
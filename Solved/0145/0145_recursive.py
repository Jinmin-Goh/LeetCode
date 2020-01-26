# Problem No.: 145
# Solver:      Jinmin Goh
# Date:        20200126
# URL: https://leetcode.com/problems/binary-tree-postorder-traversal/

import sys

# recursive solution of postorder traversal
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.find(root, [])
    def find(self, root: TreeNode, tempAns: List[int]) -> List[int]:
        if not root:
            return tempAns
        if root.left:
            tempAns = self.find(root.left, tempAns)
        if root.right:
            tempAns = self.find(root.right, tempAns)
        tempAns.append(root.val)
        return tempAns
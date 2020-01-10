# Problem No.: 105
# Solver:      Jinmin Goh
# Date:        20200110
# URL: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # inorder: (left, root, right)
        # preorder: (root, left, right)
        if not preorder:
            return None
        if len(preorder) == 1 and len(inorder) == 1:
            return TreeNode(preorder[0])
        
        root = TreeNode(preorder[0])
        inLeftList = inorder[:inorder.index(root.val)]
        inRightList = inorder[inorder.index(root.val) + 1:]
        preLeftList = preorder[1:len(inLeftList) + 1]
        preRightList = preorder[len(inLeftList) + 1:]
        root.left = self.buildTree(preLeftList, inLeftList)
        root.right = self.buildTree(preRightList, inRightList)
        
        return root        
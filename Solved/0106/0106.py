# Problem No.: 106
# Solver:      Jinmin Goh
# Date:        20200110
# URL: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # inorder: (left, root, right)
        # postorder: (left, right, root)
        if not inorder:
            return None
        if len(postorder) == 1 and len(inorder) == 1:
            return TreeNode(postorder[-1])
        
        root = TreeNode(postorder[-1])
        inLeftList = inorder[:inorder.index(root.val)]
        inRightList = inorder[inorder.index(root.val) + 1:]
        postLeftList = postorder[:len(inLeftList)]
        postRightList = postorder[len(inLeftList):-1]
        root.left = self.buildTree(inLeftList, postLeftList)
        root.right = self.buildTree(inRightList, postRightList)
        return root
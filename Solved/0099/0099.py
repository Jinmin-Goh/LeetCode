# Problem No.: 99
# Solver:      Jinmin Goh
# Date:        20200108
# URL: https://leetcode.com/problems/recover-binary-search-tree/

import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        self.inorderList = []
        self.inorder(root)
        
        big_wrong = None
        small_wrong = None
        big_wrong_node = None
        small_wrong_node = None
        for i in range(len(self.inorderList) - 1):
            if self.inorderList[i] > self.inorderList[i + 1]:
                if big_wrong == None:
                    big_wrong = self.inorderList[i]
                    small_wrong = self.inorderList[i + 1]
                else:
                    small_wrong = self.inorderList[i + 1]
        big_wrong_node = self.findNode(root, big_wrong)
        small_wrong_node = self.findNode(root, small_wrong)
        big_wrong_node.val, small_wrong_node.val = small_wrong_node.val, big_wrong_node.val
        
    def inorder(self, root: TreeNode) -> None:
        if not root.left and not root.right:
            self.inorderList.append(root.val)
            return
        if root.left:
            self.inorder(root.left)
        self.inorderList.append(root.val)
        if root.right:
            self.inorder(root.right)
    def findNode(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if root.val == val:
            return root
        else:
            return self.findNode(root.left, val) or self.findNode(root.right, val)
        
        """
        Do not return anything, modify root in-place instead.
        """
        
# Problem No.: 1008
# Solver:      Jinmin Goh
# Date:        20200421
# URL: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        head = TreeNode(preorder[0])
        walker = head
        preorder.pop(0)
        while preorder:
            temp = preorder.pop(0)
            walker = head
            while walker.left or walker.right:
                if walker.val < temp and walker.right:
                    walker = walker.right
                elif walker.val > temp and walker.left:
                    walker = walker.left
                else:
                    break
            temp = TreeNode(temp)
            if walker.val < temp.val:
                walker.right = temp
            if walker.val > temp.val:
                walker.left = temp
        return head
            
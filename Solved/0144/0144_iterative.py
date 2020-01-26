# Problem No.: 144
# Solver:      Jinmin Goh
# Date:        20200126
# URL: https://leetcode.com/problems/binary-tree-preorder-traversal/

import sys

# iterative preorder traversal solution
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
        ans = []
        stack = []
        walker = root
        while True:
            if walker.val != None:
                ans.append(walker.val)
            walker.val = None
            if (walker.left and walker.left.val != None) or (walker.right and walker.right.val != None):
                stack.append(walker)
                if walker.left and walker.left.val != None:
                    walker = walker.left
                    continue
                if walker.right and walker.right.val != None:
                    walker = walker.right
            else:
                if not stack:
                    break
                walker = stack.pop()
                
        
        return ans
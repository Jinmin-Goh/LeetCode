# Problem No.: 617
# Solver:      Jinmin Goh
# Date:        20200227
# URL: https://leetcode.com/problems/merge-two-binary-trees/

import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        ans = TreeNode(t1.val + t2.val)
        self.DFS(ans, t1, t2)
        return ans
    
    def DFS(self, root: TreeNode, t1: TreeNode, t2: TreeNode) -> None:
        if not t1 and not t2:
            return
        
        if not t1:
            if not t2.left and not t2.right:
                return
            if t2.left:
                root.left = TreeNode(t2.left.val)
                self.DFS(root.left, None, t2.left)
            if t2.right:
                root.right = TreeNode(t2.right.val)
                self.DFS(root.right, None, t2.right)
        
        elif not t2:
            if not t1.left and not t1.right:
                return
            if t1.left:
                root.left = TreeNode(t1.left.val)
                self.DFS(root.left, t1.left, None)
            if t1.right:
                root.right = TreeNode(t1.right.val)
                self.DFS(root.right, t1.right, None)
        
        else:   # both t1 and t2 is valid
            # both are leaf node
            if not (t1.left or t1.right or t2.left or t2.right):
                return
            if t1.left and t2.left:
                root.left = TreeNode(t1.left.val + t2.left.val)
                self.DFS(root.left, t1.left, t2.left)
            elif t1.left and not t2.left:
                root.left = TreeNode(t1.left.val)
                self.DFS(root.left, t1.left, None)
            elif not t1.left and t2.left:
                root.left = TreeNode(t2.left.val)
                self.DFS(root.left, None, t2.left)
            if t1.right and t2.right:
                root.right = TreeNode(t1.right.val + t2.right.val)
                self.DFS(root.right, t1.right, t2.right)
            elif t1.right and not t2.right:
                root.right = TreeNode(t1.right.val)
                self.DFS(root.right, t1.right, None)
            elif not t1.right and t2.right:
                root.right = TreeNode(t2.right.val)
                self.DFS(root.right, None, t2.right)
            
            
            
            
            
            
            
            
            
            
            
            
            
# Problem No.: 145
# Solver:      Jinmin Goh
# Date:        20200127
# URL: https://leetcode.com/problems/binary-tree-postorder-traversal/

import sys

# iterative solution of postorder traversal
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
        ans = []
        stack = []
        walker = root
        while True:
            #print(walker.val, stack, ans)
            if (walker.left and walker.left.val != None) or (walker.right and walker.right.val != None):
                stack.append(walker)
                if walker.left and walker.left.val != None:
                    walker = walker.left
                    continue
                if walker.right and walker.right.val != None:
                    walker = walker.right
                    continue
            else:
                if walker.val != None:
                    ans.append(walker.val)
                walker.val = None
                if not stack:
                    break
                walker = stack.pop()
        return ans
# Problem No.: 117
# Solver:      Jinmin Goh
# Date:        20200115
# URL: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

import sys


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        i = 0
        while True:
            self.tempNode = None
            self.dfs(root, i)
            if not self.tempNode:
                break
            i += 1
        return root
    
    def dfs(self, root: 'Node', n: int) -> None:
        if n == 0:
            if not root.left and not root.right:
                return
            if root.left:
                if not self.tempNode:
                    self.tempNode = root.left
                else:
                    self.tempNode.next = root.left
                    self.tempNode = self.tempNode.next
            if root.right:
                if not self.tempNode:
                    self.tempNode = root.right
                else:
                    self.tempNode.next = root.right
                    self.tempNode = self.tempNode.next
        else:
            if root.left:
                self.dfs(root.left, n - 1)
            if root.right:
                self.dfs(root.right, n - 1)
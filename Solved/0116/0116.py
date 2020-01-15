# Problem No.: 116
# Solver:      Jinmin Goh
# Date:        20200115
# URL: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

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
        depth = 0
        temp = root
        while temp:
            depth += 1
            temp = temp.left
        for i in range(depth - 1):
            self.tempNode = None
            self.dfs(root, i)
        return root
    
    def dfs(self, root: 'Node', i: int) -> None:
        if self.tempNode:
            print(self.tempNode.val)
        if i == 0:
            root.left.next = root.right
            if not self.tempNode:
                self.tempNode = root.right
                return
            else:
                self.tempNode.next = root.left
                self.tempNode = root.right
                return
        else:            
            self.dfs(root.left, i - 1)
            self.dfs(root.right, i - 1)
            return
        
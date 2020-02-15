# Problem No.: 297
# Solver:      Jinmin Goh
# Date:        20200216
# URL: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

import sys

# 47/48 passed and overflowError (2 ** 1000)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.depth = 0
        self.DFS(root, 0)
        data = [None] * (2 ** self.depth - 1)
        self.DFS2(root, 1, data)
        #print(self.depth, data)
        return data

    def deserialize(self, data: List[int]) -> TreeNode:
        if not data:
            return None
        nodeList = [TreeNode(i) for i in data]
        for i in range(1,self.depth):
            for j in range(2 ** i, 2 ** (i + 1)):
                if data[j - 1] != None:
                    if j % 2:
                        nodeList[j // 2 - 1].right = nodeList[j - 1]
                    else:
                        nodeList[j // 2 - 1].left = nodeList[j - 1]
        return nodeList[0]
        
    
    def DFS(self, root: TreeNode, depth: int) -> None:
        if not root:
            return
        #print(self.depth, depth, root.val)
        self.depth = max(self.depth, depth + 1)
        if root.left:
            self.DFS(root.left, depth + 1)
        if root.right:
            self.DFS(root.right, depth + 1)
        
    def DFS2(self, root: TreeNode, index: int, data: List[int]) -> None:
        if not root:
            return
        data[index - 1] = root.val
        if root.left:
            self.DFS2(root.left, 2 * index, data)
        if root.right:
            self.DFS2(root.right, 2 * index + 1, data)
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
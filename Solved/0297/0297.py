# Problem No.: 297
# Solver:      Jinmin Goh
# Date:        20200216
# URL: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

import sys

# using preorder & inorder list, using tuple
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        preList = []
        inList = []
        self.preorder(root, preList, 1)
        self.inorder(root, inList, 1)
        #print(preList, inList)
        return [preList, inList]

    def deserialize(self, data: List[List[int]]) -> TreeNode:
        if not data:
            return None
        return self.makeTree(data[0], data[1])
        
    def preorder(self, root: TreeNode, preList: List[int], depth: int) -> None:
        preList.append((root.val, depth))
        if not root:
            return
        if root.left or root.right:
            if root.left:
                self.preorder(root.left, preList, depth + 1)
            if root.right:
                self.preorder(root.right, preList, depth + 1)
        
    def inorder(self, root: TreeNode, inList: List[int], depth: int) -> None:
        if not root:
            return
        if root.left or root.right:
            if root.left:
                self.inorder(root.left, inList, depth + 1)
            inList.append((root.val, depth))
            if root.right:
                self.inorder(root.right, inList, depth + 1)
        else:
            inList.append((root.val, depth))
    
    def makeTree(self, preList: List[int], inList: List[int]) -> TreeNode:
        if not preList:
            return None
        if len(preList) == 1:
            return TreeNode(preList[0][0])
        temp = TreeNode(preList[0][0])
        leftLen = inList.index(preList[0])
        rightLen = len(inList) - leftLen - 1
        temp.left = self.makeTree(preList[1:leftLen + 1], inList[:leftLen])
        temp.right = self.makeTree(preList[leftLen + 1:], inList[leftLen + 1:])
        return temp
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
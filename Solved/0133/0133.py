# Problem No.: 133
# Solver:      Jinmin Goh
# Date:        20200122
# URL: https://leetcode.com/problems/clone-graph/

import sys

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        newNodeValList = [node.val]
        visited = [node]
        nodeList = [node]
        
        # BFS and make a copy of node values(indexes)
        while nodeList:
            tempList = []
            for i in nodeList:
                for j in i.neighbors:
                    if j not in visited:
                        newNodeValList.append(j.val)
                        visited.append(j)
                        tempList.append(j)
            nodeList = tempList[:]
        # make new node list
        newNodeValList.sort()
        newNodeList = []
        for i in newNodeValList:
            newNodeList.append(Node(i))
        
        # BFS original graph and make neighbors
        visited = [node]
        nodeList = [node]
        for i in node.neighbors:
            newNodeList[0].neighbors.append(newNodeList[i.val - 1])
        
        while nodeList:
            tempList = []
            for i in nodeList:
                for j in i.neighbors:
                    if j not in visited:
                        for k in j.neighbors:
                            newNodeList[j.val - 1].neighbors.append(newNodeList[k.val - 1])
                        visited.append(j)
                        tempList.append(j)
            nodeList = tempList[:]
        return newNodeList[0]
        
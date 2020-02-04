# Problem No.: 207
# Solver:      Jinmin Goh
# Date:        20200204
# URL: https://leetcode.com/problems/course-schedule/

import sys

# 40/42 passed and TLE
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # making adjacent list for directional graph
        self.graph = {}
        for i in prerequisites:
            if i[0] not in self.graph:
                self.graph[i[0]] = [i[1]]
            else:
                self.graph[i[0]].append(i[1])
        self.cycleFlag = False
        for i in range(numCourses):
            if self.cycleFlag:
                break
            self.DFS(i, [])
        return not self.cycleFlag
    
    def DFS(self, node: int, visitList: List[int]) -> None:
        if self.cycleFlag:
            return
        if node not in self.graph:
            return
        if node in visitList:
            self.cycleFlag = True
            return
        for i in self.graph[node]:
            visitList.append(node)
            self.DFS(i, visitList)
            visitList.pop()
        
        
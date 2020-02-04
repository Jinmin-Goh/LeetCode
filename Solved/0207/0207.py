# Problem No.: 207
# Solver:      Jinmin Goh
# Date:        20200204
# URL: https://leetcode.com/problems/course-schedule/

import sys

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # making adjacent list for directional graph
        self.graph = {}
        for i in prerequisites:
            if i[0] not in self.graph:
                self.graph[i[0]] = [i[1]]
            else:
                self.graph[i[0]].append(i[1])
        self.visit = [0] * numCourses
        # DFS for all nodes
        for i in range(numCourses):
            if not self.DFS(i):
                return False
        return True
    
    def DFS(self, node: int) -> bool:
        # in case of having loop(vitised node while DFS doing)
        if self.visit[node] == -1:
            return False
        # searched node
        if self.visit[node] == 1 or node not in self.graph:
            return True
        # search start
        self.visit[node] = -1
        for i in self.graph[node]:
            if not self.DFS(i):
                return False
        # searching complete
        self.visit[node] = 1
        return True
        
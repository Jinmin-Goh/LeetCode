# Problem No.: 210
# Solver:      Jinmin Goh
# Date:        20200307
# URL: https://leetcode.com/problems/course-schedule-ii/

import sys

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # making adjacent list for directional graph
        self.courseDict = {}
        for i in prerequisites:
            if i[0] not in self.courseDict:
                self.courseDict[i[0]] = [i[1]]
            else:
                self.courseDict[i[0]].append(i[1])
        self.ans = []
        self.visit = [0] * numCourses
        #print(self.courseDict)
        for i in range(numCourses):
            if not self.DFS(i):
                return []
        return self.ans
    
    def DFS(self, node: int) -> bool:
        if self.visit[node] == -1:  # cycle detected
            return False
        if self.visit[node] == 1:
            return True             # finished and already added to path
        self.visit[node] = -1       # visited node
        if node in self.courseDict:
            for i in self.courseDict[node]:
                if not self.DFS(i):
                    return False
        self.visit[node] = 1        # finished node
        self.ans.append(node)       # add to path
        return True
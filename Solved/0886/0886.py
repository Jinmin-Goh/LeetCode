# Problem No.: 886
# Solver:      Jinmin Goh
# Date:        20200528
# URL: https://leetcode.com/problems/possible-bipartition/

import sys

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if not dislikes:
            return True
        graph = {}
        for i in range(len(dislikes)):
            if dislikes[i][0] not in graph:
                graph[dislikes[i][0]] = [dislikes[i][1]]
            else:
                graph[dislikes[i][0]].append(dislikes[i][1])
            if dislikes[i][1] not in graph:
                graph[dislikes[i][1]] = [dislikes[i][0]]
            else:
                graph[dislikes[i][1]].append(dislikes[i][0])
        
        #print(graph)
        oddVisited = set()
        evenVisited = set()
        for t in range(N):
            if t + 1 in oddVisited or t + 1 in evenVisited or t + 1 not in graph:
                continue
            stack = [t + 1]
            oddFlag = True
            while stack:
                temp = []
                for i in stack:
                    if oddFlag:
                        if i in evenVisited:
                            return False
                        if i in oddVisited:
                            continue
                        oddVisited.add(i)
                    if not oddFlag:
                        if i in oddVisited:
                            return False
                        if i in evenVisited:
                            continue
                        evenVisited.add(i)
                    temp += graph[i]
                stack = temp[:]
                    
                oddFlag = not oddFlag
        return True
            
                    
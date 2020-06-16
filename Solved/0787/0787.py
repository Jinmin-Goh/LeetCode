# Problem No.: 787
# Solver:      Jinmin Goh
# Date:        20200616
# URL: https://leetcode.com/problems/cheapest-flights-within-k-stops/

import sys

import sys
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        if dst == src:
            return 0
        
        distance = [sys.maxsize] * n
        distance[dst] = 0
        graph = [[] for _ in range(n)]
        for data in flights:
            graph[data[1]].append([data[0], data[2]])
        stack = [dst]

        for _ in range(K + 1):
            tempList = []    
            # make distance list for every steps
            newDist = distance[:]
            while stack:
                temp = stack.pop()
                for node in graph[temp]:
                    newDist[node[0]] = min(newDist[node[0]], distance[node[0]], distance[temp] + node[1])
                    tempList.append(node[0])
                    
            tempList = list(set(tempList))
            stack = tempList[:]
            distance = newDist[:]
            
        if distance[src] == sys.maxsize:
            return -1
        else:
            return distance[src]
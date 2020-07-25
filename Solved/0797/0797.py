# Problem No.: 797
# Solver:      Jinmin Goh
# Date:        20200725
# URL: https://leetcode.com/problems/all-paths-from-source-to-target/

import sys

class Solution:
    def dfs(self, graph: List[List[int]], node: int, ans: List[int]):
        if node == len(graph) - 1:
            self.ans.append(ans)
            return
        for i in graph[node]:
            ans.append(i)
            self.dfs(graph, i, ans[:])
            ans.pop()
        
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.ans = []
        self.dfs(graph, 0, [0])
        
        print(self.ans)
        return self.ans
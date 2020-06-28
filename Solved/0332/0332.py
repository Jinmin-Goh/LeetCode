# Problem No.: 332
# Solver:      Jinmin Goh
# Date:        20200628
# URL: https://leetcode.com/problems/reconstruct-itinerary/

import sys

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if len(tickets) == 1:
            return tickets[0]
        
        posDict = {}
        posSet = set(["JFK"])
        for i in tickets:
            if i[0] not in posDict:
                posDict[i[0]] = [[i[1], True]]
            else:
                posDict[i[0]].append([i[1], True])
                posDict[i[0]].sort()
            
            if i[0] in posSet:
                posSet.remove(i[0])
            else:
                posSet.add(i[0])
            if i[1] in posSet:
                posSet.remove(i[1])
            else:
                posSet.add(i[1])
        posSet = list(posSet)
        destination = posSet[0]
        ansLen = len(tickets) + 1
        ans = ["JFK"]
        
        def backtrack(_ans: [str]) -> [str]:
            if len(_ans) == ansLen and _ans[-1] == destination:
                return _ans
            if _ans[-1] not in posDict:
                return None
            for i in posDict[_ans[-1]]:
                if not i[1]:
                    continue
                _ans.append(i[0])
                i[1] = False
                
                tempAns = backtrack(_ans)
                if tempAns:
                    return tempAns
                _ans.pop()
                i[1] = True
                
            return None
            
        ans = backtrack(ans)
        return ans
        
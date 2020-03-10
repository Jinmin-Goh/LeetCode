# Problem No.: 218
# Solver:      Jinmin Goh
# Date:        20200311
# URL: https://leetcode.com/problems/the-skyline-problem/

import sys

# good solution link: https://briangordon.github.io/2014/08/the-skyline-problem.html
# time: O(n log n)
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []
        buildingDict = {}
        # make dict with key: position, value: building index
        for i in range(len(buildings)):
            if buildings[i][0] not in buildingDict:
                buildingDict[buildings[i][0]] = [i]
            else:
                buildingDict[buildings[i][0]].append(i)
            if buildings[i][1] not in buildingDict:
                buildingDict[buildings[i][1]] = [i]
            else:
                buildingDict[buildings[i][1]].append(i)
        ans = []
        indexList = list(buildingDict.keys())
        indexList.sort()
        currBuildingSet = set() # set for (buinding #, first index)
        currHeightSet = set()   # set for (height, building #)
        maxVal = 0
        for i in indexList:
            checkFlag = False   # if true check maxVal
            ansFlag = False     # if true add ans
            for build in buildingDict[i]:
                # if building is not in set
                if (build, buildings[build][0]) not in currBuildingSet:
                    currBuildingSet.add((build, i))
                    currHeightSet.add((buildings[build][2], build))
                    # update maxVal
                    if maxVal < buildings[build][2]:
                        maxVal = buildings[build][2]
                        ansFlag = True
                # if building is in set
                else:
                    currBuildingSet.remove((build, buildings[build][0]))
                    currHeightSet.remove((buildings[build][2], build))
                    if maxVal == buildings[build][2]:
                        checkFlag = True
            if checkFlag:
                if currHeightSet:
                    temp = max(currHeightSet)[0]
                else:
                    temp = 0
                if temp < maxVal:
                    ansFlag = True
                    maxVal = temp
            if ansFlag:
                ans.append([i, maxVal])
        return ans
            
            
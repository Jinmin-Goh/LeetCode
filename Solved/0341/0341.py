# Problem No.: 341
# Solver:      Jinmin Goh
# Date:        20200323
# URL: https://leetcode.com/problems/flatten-nested-list-iterator/

import sys

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [[nestedList, 0]]
    
    def next(self) -> int:
        print("Next")
        self.hasNext()
        numList = self.stack[-1][0]
        iterator = self.stack[-1][1]
        self.stack[-1][1] += 1
        return numList[iterator].getInteger()
    
    def hasNext(self) -> bool:
        s = self.stack
        while s:
            print("s:",s, "\n")
            numList = s[-1][0]
            iterator = s[-1][1]
            print(numList, iterator, "\n")
            if iterator == len(numList):
                s.pop()
            else:
                temp = numList[iterator]
                if temp.isInteger():
                    return True
                s[-1][1] += 1
                s.append([temp.getList(), 0])
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
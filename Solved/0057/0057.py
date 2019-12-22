# Problem No.: 57
# Solver:      Jinmin Goh
# Date:        20191222
# URL: https://leetcode.com/problems/insert-interval/

import sys

class Solution(object):
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        # insert at front
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        # insert at rear
        if newInterval[0] > intervals[len(intervals) - 1][1]:
            return intervals + [newInterval]
        temp = None
        for i in range(0,len(intervals)):
            # no merging
            if intervals[i][1] < newInterval[0] and newInterval[1] < intervals[i + 1][0]:
                return intervals[:i+1] + [newInterval] + intervals[i+1:]
            
            if intervals[0][0] > newInterval[0]:
                intervals[0][0] = newInterval[0]
            if intervals[len(intervals) - 1][1] < newInterval[1]:
                intervals[len(intervals) - 1][1] = newInterval[1]
            
            # completely included
            if intervals[i][1] >= newInterval[1] and intervals[i][0] <= newInterval[0]:
                return intervals
            # overlapped
            if newInterval[0] < intervals[i][1] or intervals[i][0] <= newInterval[0] <= intervals[i][1] <= newInterval[1]:
                temp = i
                while i < len(intervals) - 1 and not(intervals[i][0] <= newInterval[1] <= intervals[i][1] or newInterval[1] < intervals[i + 1][0]):
                    i += 1
                print(intervals,temp, i)
                return intervals[:temp] + [[min(newInterval[0],intervals[temp][0]),max(newInterval[1],intervals[i][1])]] + intervals[i + 1:]
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
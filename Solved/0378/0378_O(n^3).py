# Problem No.: 378
# Solver:      Jinmin Goh
# Date:        20200327
# URL: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

# good solution links
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85193/Binary-Search-Heap-and-Sorting-comparison-with-concise-code-and-1-liners-Python-72-ms
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85170/O(n)-from-paper.-Yes-O(rows).

import sys

# time: O(n^3) / space: O(n) / n: ncol or nrow
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        numList = [matrix[0].pop(0)]
        if not matrix[0]:
            matrix.pop(0)
        while len(numList) < k:
            #print(numList, matrix)
            temp = matrix[-1][-1]
            ptr = 0
            for i in range(len(matrix)):
                if matrix[i][0] <= temp:
                    temp = matrix[i][0]
                    ptr = i
            numList.append(matrix[ptr].pop(0))
            if not matrix[ptr]:
                matrix.pop(ptr)
        return numList[-1]
        
        # python default sort function
        """
        ans = []
        for i in matrix:
            ans += i
        ans.sort()
        return ans[k - 1]
        """
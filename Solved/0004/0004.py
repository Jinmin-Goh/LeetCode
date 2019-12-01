# Problem No.: 4
# Solver:      Jinmin Goh
# Date:        20191201
# URL: https://leetcode.com/problems/median-of-two-sorted-arrays/

import sys

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        tot_list = nums1 + nums2
        tot_list.sort()
        if len(tot_list) % 2:
            return tot_list[len(tot_list) // 2]
        else:
            return (float(tot_list[len(tot_list) // 2]) + tot_list[len(tot_list) // 2 - 1]) / 2

        """
        tot_len = len(nums1) + len(nums2)
        p1 = 0
        p2 = 0
        
        # odd case
        if tot_len % 2 == 1:
            while (p1 + p2 + 2) < (tot_len // 2 + 1):
                if nums1[p1] > nums2[p2]:
                    p2 += 1
                else:
                    p1 += 1
            return float(max(nums1[p1] , nums2[p2]))
        else:
            while (p1 + p2 + 2) < (tot_len // 2 + 1):
                if nums1[p1] > nums2[p2]:
                    p2 += 1
                else:
                    p1 += 1
            if p1 == len(nums1) - 1 and p2 == len(nums2) - 1:
                return (float(nums1[p1]) + nums2[p2]) / 2
            elif p1 == len(nums1) - 1:
                return min((float(nums1[p1]) + nums2[p2]) / 2, (float(nums2[p2 + 1]) + nums2[p2]) / 2)
            elif p2 == len(nums2) - 1:
                return min((float(nums1[p1]) + nums2[p2]) / 2, (float(nums1[p1]) + nums1[p1 + 1]) / 2)
            else:
                return min((float(nums1[p1]) + nums2[p2]) / 2, (float(nums1[p1]) + nums1[p1 + 1]) / 2, (float(nums2[p2 + 1]) + nums2[p2]) / 2)
        """    
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
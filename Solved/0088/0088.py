# Problem No.: 88
# Solver:      Jinmin Goh
# Date:        20200105
# URL: https://leetcode.com/problems/merge-sorted-array/

import sys

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0:
            return
        if m == 0:
            for i, val in enumerate(nums2):
                nums1[i] = val
            return
        m_cnt = m - 1
        n_cnt = n - 1
        pos = len(nums1) - 1
        while m_cnt >= 0 and n_cnt >= 0:
            if nums1[m_cnt] > nums2[n_cnt]:
                nums1[pos] = nums1[m_cnt]
                m_cnt -= 1
                pos -= 1
            else:
                nums1[pos] = nums2[n_cnt]
                n_cnt -= 1
                pos -= 1
        if m_cnt < 0:
            while n_cnt >= 0:
                nums1[n_cnt] = nums2[n_cnt]
                n_cnt -= 1
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
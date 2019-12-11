# Problem No.: 25
# Solver:      Jinmin Goh
# Date:        20191211
# URL: https://leetcode.com/problems/reverse-nodes-in-k-group/submissions/

import sys

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        temp_list = []
        ans_head = None
        ans_walker = None
        walker = head
        temp_node = None
        while walker:
            while walker and len(temp_list) < k:
                temp_list.append(walker.val)
                walker = walker.next
            print(temp_list)
            if len(temp_list) == k:
                if not ans_head:
                    ans_head = ListNode(temp_list.pop())
                    ans_walker = ans_head
                while temp_list:
                    temp_node = ListNode(temp_list.pop())
                    ans_walker.next = temp_node
                    ans_walker = ans_walker.next
            else:
                if not ans_head:
                    return head
                while temp_list:
                    temp_node = ListNode(temp_list.pop(0))
                    ans_walker.next = temp_node
                    ans_walker = ans_walker.next
        return ans_head
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
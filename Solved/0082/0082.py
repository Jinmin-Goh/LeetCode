# Problem No.: 82
# Solver:      Jinmin Goh
# Date:        20200101
# URL: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

import sys

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p_ans = None
        temp_val = None
        duplFlag = False
        p_stay = head
        p_move = head
        ans = None
        while p_move:
            if temp_val == None:
                temp_val = p_move.val
                p_move = p_move.next
                continue
            if p_move.val == temp_val:
                duplFlag = True
                p_move = p_move.next
                continue
            if p_move.val != temp_val:
                if not duplFlag:
                    if not ans:
                        ans = ListNode(temp_val)
                        p_ans = ans
                    else:
                        p_ans.next = ListNode(temp_val)
                        p_ans = p_ans.next
                        p_stay = p_move
                else:
                    duplFlag = False
                temp_val = p_move.val
                p_move = p_move.next
        if not duplFlag:
            if not ans:
                ans = ListNode(temp_val)
            else:
                p_ans.next = ListNode(temp_val)
        return ans
            
                
                
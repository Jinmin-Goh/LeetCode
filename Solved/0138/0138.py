# Problem No.: 138
# Solver:      Jinmin Goh
# Date:        20200123
# URL: https://leetcode.com/problems/copy-list-with-random-pointer/

import sys

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        ans = None
        walker = head
        ansWalker = None
        cnt = 0
        # make copy of next
        while walker:
            if not ans:
                temp = Node(head.val)
                ans = temp
                ansWalker = ans
                walker = walker.next
            else:
                temp = Node(walker.val)
                ansWalker.next = temp
                walker = walker.next
                ansWalker = ansWalker.next
            cnt += 1
        # apply random index from original to copied graph
        walker = head
        ansWalker = ans
        while walker:
            if not walker.random:
                walker = walker.next
                ansWalker = ansWalker.next
            else:
                temp = walker.random
                tempcnt = 0
                while temp:
                    temp = temp.next
                    tempcnt += 1
                tempcnt = cnt - tempcnt
                temp = ans
                while tempcnt > 0:
                    temp = temp.next
                    tempcnt -= 1
                ansWalker.random = temp
                walker = walker.next
                ansWalker = ansWalker.next
        return ans
                
            
        
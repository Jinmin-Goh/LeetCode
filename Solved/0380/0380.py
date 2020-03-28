# Problem No.: 380
# Solver:      Jinmin Goh
# Date:        20200328
# URL: https://leetcode.com/problems/insert-delete-getrandom-o1/

import sys

# time: O(1)

class RandomizedSet:
    def __init__(self):
        self.randSet = set()

    def insert(self, val: int) -> bool:
        flag = False
        if val not in self.randSet:
            flag = True
            self.randSet.add(val)
        return flag

    def remove(self, val: int) -> bool:
        flag = False
        if val in self.randSet:
            flag = True
            self.randSet.remove(val)
        return flag

    def getRandom(self) -> int:
        return random.sample(self.randSet, 1)[0]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
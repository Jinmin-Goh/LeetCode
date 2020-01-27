# Problem No.: 146
# Solver:      Jinmin Goh
# Date:        20200127
# URL: https://leetcode.com/problems/lru-cache/

import sys

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key: int) -> int:
        if not self.cache:
            return -1
        if key in self.cache:
            tempKey = key
            tempVal = self.cache[key]
            del self.cache[key]
            self.cache[tempKey] = tempVal
            if self.order[0] == key:
                self.order.pop(0)
                self.order.append(key)
            return tempVal
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
            
            self.order.pop(0)
        elif len(self.cache) >= self.capacity:            
            del self.cache[self.order.pop(0)]
        self.cache[key] = value
        self.order.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
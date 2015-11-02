# https://leetcode.com/problems/lru-cache/

# Design and implement a data structure for Least Recently Used (LRU) cache. 
# It should support the following operations: get and set.

# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.

# set(key, value) - Set or insert the value if the key is not already present. 
# When the cache reached its capacity, it should invalidate the least recently 
# used item before inserting a new item.

import collections

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dict = collections.OrderedDict()

    def get(self, key):
        """
        :rtype: int
        """
        value = self.dict.pop(key, -1)
        if value is not -1:
            self.dict[key] = value
        return value

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        self.dict.pop(key, -1)
        self.dict[key] = value
        
        if len(self.dict) > self.capacity:
            self.dict.popitem(False)



cache = LRUCache(2)
cache.set(2,1)
cache.set(1,2)
print cache.get(2), 1
cache.set(4,1)
print cache.get(1), -1
print cache.get(2), 1

print "-"*10
cache2 = LRUCache(2)
cache2.set(2,1)
cache2.set(1,2)
cache2.set(2,3)
cache2.set(4,1)
print cache2.get(1), -1
print cache2.get(2), 3
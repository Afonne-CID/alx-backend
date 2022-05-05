#!/usr/bin/env python3
'''LIFOCache module
'''
from collections import deque


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''Inherits from `BaseCaching`
    '''
    def __init__(self):
        '''Initializes class
        '''
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        '''Assigns to `self.cache_data` the `item` value for `key`
        '''
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif self.is_full():
                self.evict()
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        '''Returns the value in `self.cache_data` linked to `key`
        '''
        return self.cache_data.get(key, None)

    def is_full(self):
        '''Checks if # of items in `self.cache_data`
           is higher than BaseCaching.MAX_ITMES
        '''
        return len(self.cache_data) >= self.MAX_ITEMS

    def evict(self):
        '''Pops off the first item and prints DISCARD
        '''
        popped = self.queue.pop()
        del self.cache_data[popped]
        print('DISCARD: {}'.format(popped))

#!/usr/bin/env python3
'''BasicCache module
'''


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''Inherits from BaseCaching
    '''
    def put(self, key, item):
        '''Assign to to `self.cache_data` the `item` value for `key`
        '''
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        '''Returns the value in `self.cache_data` linked to key
        '''
        return self.cache_data.get(key, None)

#!usr/bin/env python3
"""Module to implement basic cache system"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Creates a basic cache with no limit """

    def put(self, key, item):
        """add an item to cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """retrieves item from cache"""
        if key is None:
            return None
        return self.cache_data.get(key, None)

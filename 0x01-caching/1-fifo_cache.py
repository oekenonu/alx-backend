#!usr/bin/env python3
"""Module that implements fifo caching policy"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Creates a fifo cache with limit """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """add an item to cache"""

        if key in self.cache_data:
            del self.cache_data[key]

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = next(iter(self.cache_data))
            del self.cache_data[discard]
            print(f"DISCARD {discard}")

        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """retrieves item from cache"""
        if key is None:
            return None
        return self.cache_data.get(key, None)

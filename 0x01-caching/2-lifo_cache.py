#!usr/bin/env python3
"""Module that implements LILO caching policy"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache is a caching system that uses LIFO algorithm. """

    def __init__(self):
        """ Initialize the class, calling the parent class' constructor. """
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """
        Add an item in the cache using LIFO algorithm.
        If the cache exceeds MAX_ITEMS, remove the last added item.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.last_key is not None:
                del self.cache_data[self.last_key]
                print(f"DISCARD: {self.last_key}")

        # Update the last key to the current key
        self.last_key = key

    def get(self, key):
        """
        Get an item by key from the cache.
        Return None if the key is not present in the cache.
        """
        return self.cache_data.get(key, None)

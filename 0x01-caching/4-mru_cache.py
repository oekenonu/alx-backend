#!usr/bin/env python3
"""MRU Cache Module"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache is a caching system that uses the MRU algorithm. """

    def __init__(self):
        """ Initialize the class, calling the parent class' constructor. """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item in the cache using MRU algorithm.
        If the cache exceeds MAX_ITEMS, remove the most recently used item.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)

        self.cache_data[key] = item
        self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            mru_key = self.order.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

    def get(self, key):
        """
        Get an item by key from the cache.
        Return None if the key is not present in the cache.
        """
        if key is None or key not in self.cache_data:
            return None

        # Update the order of the key to mark it as recently used
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]

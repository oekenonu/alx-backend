#!usr/bin/env python3
"""LRU Cache Module"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache is a caching system that uses the LRU algorithm. """

    def __init__(self):
        """ Initialize the class, calling the parent class' constructor. """
        super().__init__()
        self.order = []  # This list will maintain the order of access

    def put(self, key, item):
        """
        Add an item in the cache using LRU algorithm.
        If the cache exceeds MAX_ITEMS, remove the least recently used item.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)

        self.cache_data[key] = item
        self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

    def get(self, key):
        """
        Get an item by key from the cache.
        Return None if the key is not present in the cache.
        """
        if key is None or key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]

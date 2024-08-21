#!usr/bin/env python3
"""Module that implements LFU caching policy"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache is a caching system that uses the LFU algorithm. """

    def __init__(self):
        """ Initialize the class, calling the parent class' constructor. """
        super().__init__()
        self.frequency = {}
        self.order = {}

    def put(self, key, item):
        """
        Add an item in the cache using LFU algorithm.
        If the cache exceeds MAX_ITEMS, remove the least frequently used item.
        If there's a tie, use LRU to remove the least recently used item.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used key
                min_freq = min(self.frequency.values())
                lfu_keys = [k for k, v in self.frequency.items()
                            if v == min_freq]

                if len(lfu_keys) > 1:
                    lru_key = min(lfu_keys, key=lambda k: self.order[k])
                else:
                    lru_key = lfu_keys[0]

                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                del self.order[lru_key]
                print(f"DISCARD: {lru_key}")

            # Add the new key and item
            self.cache_data[key] = item
            self.frequency[key] = 1

        # Update the order to reflect the most recent access
        self.order[key] = len(self.order)

    def get(self, key):
        """
        Get an item by key from the cache.
        Return None if the key is not present in the cache.
        """
        if key is None or key not in self.cache_data:
            return None

        # Increase the frequency of the key and update its order
        self.frequency[key] += 1
        self.order[key] = len(self.order)
        return self.cache_data[key]

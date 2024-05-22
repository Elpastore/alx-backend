#!/usr/bin/env python3
"""
3-lru_cache module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    LRUCaching class
    """
    def __init__(self):
        """
        init method
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        add data in the cache
        """
        if key is None and item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # remove the least recently used
            lru_item, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {lru_item}")

        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """
        retrieve data
        """
        if key is None or key not in self.cache_data:
            return None

        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)

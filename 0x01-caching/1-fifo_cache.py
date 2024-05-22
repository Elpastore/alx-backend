#!/usr/bin/env python3
"""
1-fifo_cache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCaching class
    """
    def __init__(self):
        """
        init method
        """
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """
        method that add data in the cache
        """
        if key is None or item is None:
            return
        else:
            if key in self.cache_order and len(self.cache_data) <= BaseCaching.MAX_ITEMS:
                oldest_key = self.cache_order.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")
            self.cache_data[key] = item
            self.cache_order.append(key)

    def get(self, key):
        """
        method that retrieve data
        """
        return self.cache_data.get(key, None)

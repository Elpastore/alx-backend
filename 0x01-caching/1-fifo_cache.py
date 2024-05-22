#!/usr/bin/env python3
"""
1-fifo_cache module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """
    FIFOCaching class
    """
    def __init__(self):
        """
        init method
        """
        super().__init__()
        # self.cache_order = []
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        method that add data in the cache
        """
        if key is None or item is None:
            return
        length_cache = len(self.cache_data)
        if length_cache >= BaseCaching.MAX_ITEMS:
            # oldest_key = self.cache_order.pop(0)
            oldest_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {oldest_key}")
        self.cache_data[key] = item
        # self.cache_order.append(key)

    def get(self, key):
        """
        method that retrieve data
        """
        return self.cache_data.get(key, None)

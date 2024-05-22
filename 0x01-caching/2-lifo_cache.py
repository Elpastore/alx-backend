#!/usr/bin/env python3
"""
2-lifo_cache module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """
    LIFOCache class
    """
    def __init__(self):
        """
        init method
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        method that add item in cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_item, _ = self.cache_data.popitem(last=True)
            print(f"DISCARD: {last_item}")
        self.cache_data[key] = item

    def get(self, key):
        """
        method that retrieve data
        """
        return self.cache_data.get(key, None)

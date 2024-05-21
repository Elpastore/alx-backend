#!/usr/bin/env python3
"""
0-basic_cache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class
    """
    def __init__(self):
        """
        init method
        """
        super().__init__()

    def put(self, key, item):
        """
        method that add data to the cache dictionnary
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        method that retrieve data
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)

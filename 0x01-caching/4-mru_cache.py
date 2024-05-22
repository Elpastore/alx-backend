#!/usr/bin/env python3
"""
4-mru_cache module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    MRUCaching class
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
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # remove the most recently used
                mru_item, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {mru_item}")

            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        retrieve data
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)

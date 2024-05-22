#!/usr/bin/env python3
"""
100-lfu_cache module
"""
from base_caching import BaseCaching
from collections import OrderedDict, defaultdict


class LFUCache(BaseCaching):
    """
    LFUCache class
    """
    def __init__(self):
        """
        init method
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.count = defaultdict(int)
        self.usage_order = OrderedDict()

    def put(self, key, item):
        """
        add item to the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the existing item and its usage
            self.cache_data[key] = item
            self.count[key] += 1
            self.usage_order.move_to_end(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the least frequently used key
                min_count = min(self.count.values())
                lfu_keys = [k for k, v in self.count.items() if v == min_count]

                # If there are multiple LFU items
                # use LRU strategy to choose one
                if len(lfu_keys) > 1:
                    lfu_key = None
                    for k in self.usage_order:
                        if k in lfu_keys:
                            lfu_key = k
                            break
                else:
                    lfu_key = lfu_keys[0]

                # Remove the least frequently used
                # (and least recently used if tie) item
                del self.cache_data[lfu_key]
                del self.count[lfu_key]
                del self.usage_order[lfu_key]
                print(f"DISCARD: {lfu_key}")

            # Add the new item to the cache
            self.cache_data[key] = item
            self.count[key] = 1
            self.usage_order[key] = None

    def get(self, key):
        """
        Retrieve an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None

        # Update the access count and usage order
        self.count[key] += 1
        self.usage_order.move_to_end(key)
        return self.cache_data[key]

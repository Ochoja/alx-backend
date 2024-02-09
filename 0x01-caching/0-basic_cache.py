#!/usr/bin/env python3
"""Base caching"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Get and insert cache data"""

    def put(self, key, item):
        """put item in cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get item from cache"""
        return self.cache_data.get(key)

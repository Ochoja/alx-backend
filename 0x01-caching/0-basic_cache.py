#!/usr/bin/env python3
"""Base caching"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Caching system"""

    def put(self, key, item):
        """put item"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get item"""
        return self.cache_data[key]

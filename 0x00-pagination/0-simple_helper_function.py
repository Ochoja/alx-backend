#!/usr/bin/env/ python3
"""Simple helper function for pagination"""


def index_range(page: int, page_size: int):
    """Returns start and end index"""
    return ((page_size * page) - page_size, page_size * page)

#!/usr/bin/env/ python3
"""Simple helper function for pagination"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns start and end index"""
    return ((page - 1) * page_size, page_size * page)

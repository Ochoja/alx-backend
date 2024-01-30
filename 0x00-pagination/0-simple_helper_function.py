#!/usr/bin/env/ python3
"""Simple helper function for pagination"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns start and end index"""
    start = (page - 1) - page_size
    end = page_size * page

    return (start, end)

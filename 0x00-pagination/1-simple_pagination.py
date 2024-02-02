#!/usr/bin/env python3
"""Simple pagination"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns start and end index"""
    start = (page_size * page) - page_size
    end = page_size * page

    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Fetch data on a page base on the page number and page size"""
        filename = 'Popular_Baby_Names.csv'
        rows = []

        assert (isinstance(page, int) and isinstance(page_size, int))
        assert (page > 0 and page_size > 0)

        indexes = index_range(page, page_size)  # get start and end index

        with open(filename, 'r') as baby_names:
            csvreader = list(csv.reader(baby_names))

            # ignore header by adding 1 to index
            for row in csvreader[indexes[0] + 1: indexes[1] + 1]:
                rows.append(row)

            return rows

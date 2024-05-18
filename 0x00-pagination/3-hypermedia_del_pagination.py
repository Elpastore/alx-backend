#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        init method
        """
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Deletion-resilient hypermedia pagination
        """
        data = self.indexed_dataset()
        # validation index
        assert isinstance(index, int)
        assert isinstance(page_size, int) and page_size > 0
        assert 0 <= index < len(data)

        start_index = index if index else 0
        next_index = None
        page_data = []  # will contain data to be displayed
        count = 0

        for i, item in data.items():
            if i >= start_index and count < page_size:
                page_data.append(item)
                count += 1
                continue
            if count == page_size:
                next_index = i
                break

        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': page_data
        }

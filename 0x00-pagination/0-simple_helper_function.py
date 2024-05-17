#!/usr/bin/env python3
"""
0-simple_helper_function module
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    return a tuple of size two containing a start index and an end index
    """
    start_index: int = (page - 1) * page_size
    end_index: int = start_index + page_size

    return (start_index, end_index)

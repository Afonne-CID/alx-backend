#!/usr/bin/env python3
'''Task 0's module
'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''returns a start and end index corresponding to the range of indexes
    to return in a list for the given pagination parameters- page and page_size
    '''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)

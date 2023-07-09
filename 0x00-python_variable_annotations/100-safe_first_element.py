#!/usr/bin/env python3
'''Retrieves the first element of a sequence if it exists.'''
from typing import Any, Sequence, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None

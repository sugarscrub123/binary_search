from .validation import _validate_item, _validate_criteria
from .py_implement import _perform_binary_search

def bin_search(item, criteria, mode = 'py'):
    """
    Performs a binary search on an ORDERED list or tuple of single type.

    Args:
        item ([list, tuple]): Item to be searched.
        criteria ([int, float]): Single search criteria.
        mode ([string], optional): Mode (C or Python) to search in.

    Raises:
        ValueError: Missing arguments (in validation functions from validation module)
        ValueError: Invalid mode argument

    Returns:
        res: Result of binary search in either implementation. Returns None if target was not found, and all indices of occurences otherwise. 
    """
    _validate_item(inpt = item)
    _validate_criteria(inpt = criteria)

    if mode == 'py':
        if type(item) == tuple:
            item = list(item)
        res = _perform_binary_search(item, criteria, 0, len(item))
    elif mode == 'c':
        pass
    else:
        raise ValueError('Invalid mode argument: {}'.format(mode))

    
    return res







def _perform_binary_search(seq, target, start, end):
    """
    Performs a binary search on a sorted parameter seq and returns None if target was not found and the index if it was.

    Args:
        seq ([list, tuple]): A list or tuple to search.
        target ([int, float]): An integer or floatint point value to search for.
        start ([int]): Starting index 
        end ([int]): Ending index

    Returns:
        None: Returns None if the value was not found.
        int: Returns an int index of the first instance of the value if it was found.
    """

    i = (start + end) // 2

    if not seq[start:end]:
        # if the sequence is empty, the target value wasn't found. 
        return None

    elif seq[i] == target:
        # return the index if it's the target value.
        return i

    elif target > seq[i]:
        # pop out the bottom half of the list
        return _perform_binary_search(seq, target, i + 1, end)
    
    elif target < seq[i]:
        # pop out the top half of the list
        return _perform_binary_search(seq, target, start, i)

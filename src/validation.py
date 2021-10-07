
def _validate_item(inpt):
    """
    Validates sequence to be searched through.

    Args:
        inpt (any): Sequence to be searched

    Raises:
        ValueError: Invalid types (i.e. not tuple or list) inputted by user

    Returns:
        bool: Returns True if the sequence is valid, None (and raises an error) otherwise
    """
    item_type = type(inpt)
    if not item_type == list and not item_type == tuple:
        raise ValueError('Invalid type -- accepts only tuples and lists.')
    return True

def _validate_criteria(inpt):
    """
    Validates criteria to be searched for.

    Args:
        inpt (any): Criteria to search for

    Raises:
        ValueError: Invalid types (i.e. not int or float) inputted by user.

    Returns:
        bool: Returns True if the sequence is valid, None (and raises an error) otherwise
    """
    criteria_type = type(inpt)
    if not criteria_type == int and not criteria_type == float:
        raise ValueError('Invalid type -- accepts only ints and floats.')
    return True
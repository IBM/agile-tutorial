def square_list(integer_list):
    """
    Takes the square of every integer in the list.

    Receives
    --------
    integer_list : list
        List of integer values.

    Returns
    -------
    squared_list : list
        List of the squares of integer values.
    """

    squared_list = [x**2 for x in integer_list]
    integer_list.clear()
    integer_list.extend(squared_list)
    return integer_list

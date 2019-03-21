def double_list(integer_list):
    """
    Multiplies every integer in the list by 2.

    Receives
    --------
    integer_list : list
        List of integer values.

    Returns
    -------
    doubled_list : list
        List of integer values multiplied by 2.
    """

    doubled_list = [2*x for x in integer_list]
    integer_list.clear()
    integer_list.extend(doubled_list)
    return integer_list

def csv_to_list(csv_string):
    """
    Converts a string with comma-separated integer values to a Python list of integers.

    Receives
    --------
    csv_string : string
        Comma-separated integer values (stored as strings).

    Returns
    -------
    integer_list : list
        List of integer values.
    """

    string_list = csv_string.split(',')
    integer_list = list(map(int, string_list))
    return integer_list

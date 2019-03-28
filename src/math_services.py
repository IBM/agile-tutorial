import numpy as np


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


def mean(integer_list):
    """
    Calculates the mean of the list of integers.

    Receives
    --------
    integer_list : list
        List of integers.

    Returns
    -------
    mean : float
        Mean value of the list.
    """

    integer_array = np.array(integer_list, dtype=int)
    return np.mean(integer_array).astype(float)


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


def triple_list(integer_list):
    """
    Multiplies every integer in the list by 3.

    Receives
    --------
    integer_list : list
        List of integer values.

    Returns
    -------
    tripled_list : list
        List of integer values multiplied by 3.
    """

    tripled_list = [3*x for x in integer_list]
    integer_list.clear()
    integer_list.extend(tripled_list)
    return integer_list

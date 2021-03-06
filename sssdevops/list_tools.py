"""
Main python file for the sssdevops example
"""


def mean(num_lst):
    """
    Calculates teh mean of a list of numbers

    Parameters
    ----------
    num_lst : list of int or float
    List of numbers to calculate the average of

    Returns
    -------
    float of the average/mean of num_lst

    Examples
    --------
    >>> mean([1, 2, 3, 4, 5])
    3.0
    """

    return sum(num_lst) / len(num_lst)  #built-in functions!

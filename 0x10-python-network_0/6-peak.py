#!/usr/bin/python3
"""module to find a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """
    function that finds a peak in a list of unsorted integers.
    """

    if list_of_integers is None or list_of_integers == []:
        return None

    l1 = 0
    length_int = len(list_of_integers)
    mid = ((length_int - l1) // 2) + l1
    mid = int(mid)

    if length_int == 1:
        return list_of_integers[0]

    if length_int == 2:
        return max(list_of_integers)

    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])

#!/usr/bin/python3
''' The function that finds a peak in a list of unsorted integers.'''


def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    low = 0
    high = len(list_of_integers) - 1

    while low <= high:
        mid = (low + high) // 2
        left = list_of_integers[mid - 1] if mid > 0 else float("-inf")
        right = list_of_integers[mid + 1] if mid < len(list_of_integers) - 1 else float("-inf")
        if list_of_integers[mid] >= left and list_of_integers[mid] >= right:
            return list_of_integers[mid]
        elif list_of_integers[mid] < right:
            low = mid + 1
        else:
            high = mid - 1

#!/usr/bin/python3


"""a function that prints the first x elements of a list and only integers."""


def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        i = 0
        while count != x:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
            i += 1
    except(ValueError, TypeError, IndexError):
        i += 1
    print()
    return count

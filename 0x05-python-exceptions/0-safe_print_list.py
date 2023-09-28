#!/usr/bin/python3


"""a function that prints x elements of a list."""


def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        i = 0
        while count != x:
            print("{}".format(my_list[i]), end="")
            count += 1
            i += 1
    except IndexError:
        pass
    finally:
        print()
        return count

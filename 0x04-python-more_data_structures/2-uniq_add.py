#!/usr/bin/python3

def uniq_add(my_list=[]):
    my_set = set(my_list)
    new_list = list(my_set)
    res = sum(new_list)
    return res

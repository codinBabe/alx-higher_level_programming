#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    for v in new_dictionary:
        new_dictionary[v] *= 2
    return new_dictionary

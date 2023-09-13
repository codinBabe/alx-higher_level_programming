#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None

    v = max(a_dictionary, key=lambda a: a_dictionary[a])
    return v

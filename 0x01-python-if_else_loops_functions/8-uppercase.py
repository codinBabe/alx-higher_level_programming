#!/usr/bin/python3

def uppercase(str):
    upper = ""
    for c in str:
        if 'a' <= c <= 'z':
            upper_c = chr(ord(c) -ord('a') + ord('A'))
            upper += upper_c
        else:
            upper += c
    print("{}".format(upper))
